from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import List

from app.models import ProductOut, ProductsResponse
from app.errors import ApiError, api_error_response
from app.services import ProductService

# Inicialización de la aplicación
app = FastAPI(title="MELI API Products", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service = ProductService()


# Manejadores globales de errores
@app.exception_handler(ApiError)
async def handle_api_error(request, exc: ApiError):
    return JSONResponse(
        status_code=exc.status_code,
        content=api_error_response(exc)
    )

@app.exception_handler(RequestValidationError)
async def handle_validation_error(request, exc: RequestValidationError):
    details = exc.errors()
    err = ApiError.validation("Error de validación en los parámetros de entrada", details)
    return JSONResponse(status_code=422, content=api_error_response(err))

@app.exception_handler(StarletteHTTPException)
async def handle_http_error(request, exc: StarletteHTTPException):
    err = ApiError(message=exc.detail, status_code=exc.status_code, type="http_error")
    return JSONResponse(status_code=err.status_code, content=api_error_response(err))

@app.exception_handler(Exception)
async def handle_unexpected_error(request, exc: Exception):
    print(f"Unhandled error: {exc}")
    err = ApiError.internal("Error interno del servidor")
    return JSONResponse(status_code=500, content=api_error_response(err))


# Endpoints de la API
@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/products", response_model=ProductsResponse)
def list_products(
    q: str | None = Query(None),
    min_price: float | None = Query(None, ge=0),
    max_price: float | None = Query(None, ge=0),
    min_rating: float | None = Query(None, ge=0, le=5),
    sort_by: str | None = Query(None, pattern="^(name|price|rating)$"),
    order: str = Query("asc", pattern="^(asc|desc)$"),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    try:
        return service.list_products(q, min_price, max_price, min_rating, sort_by, order, limit, offset)
    except Exception as e:
        from app.errors import ApiError
        raise ApiError.internal(f"Error interno del servidor: {e}")

@app.get("/api/products/{product_id}", response_model=ProductOut)
def get_product(product_id: str):
    return service.get_product(product_id)


@app.get("/api/compare")
def compare(ids: List[str] = Query(..., description="IDs de productos a comparar")):
    if len(ids) < 2:
        raise ApiError.bad_request("Se requieren al menos 2 IDs para comparar")
    return service.compare_products(ids)
