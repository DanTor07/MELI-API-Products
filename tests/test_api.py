from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test de estado y listado
def test_health():
    """Verifica que el endpoint /api/health funcione correctamente"""
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.json()
    assert data == {"status": "ok"}


def test_get_products_list():
    """Debe devolver la lista completa de productos con total e items"""
    res = client.get("/api/products")
    assert res.status_code == 200
    data = res.json()
    assert "total" in data
    assert "items" in data
    assert isinstance(data["items"], list)
    assert len(data["items"]) > 0


def test_get_products_with_filters():
    """Debe filtrar correctamente por rango de precio"""
    res = client.get("/api/products?min_price=50&max_price=1000")
    assert res.status_code == 200
    data = res.json()
    for p in data["items"]:
        assert 50 <= p["price"] <= 1000


# Tests de detalle de producto
def test_get_product_by_valid_id():
    """Debe devolver un producto válido"""
    res = client.get("/api/products/P001")
    assert res.status_code == 200
    data = res.json()
    assert data["id"] == "P001"
    assert "price" in data
    assert "rating" in data


def test_get_product_not_found():
    """Debe devolver error 404 para ID inexistente"""
    res = client.get("/api/products/UNKNOWN")
    assert res.status_code == 404
    data = res.json()
    assert "error" in data
    assert data["error"]["type"] == "not_found"


# Test de comparación
def test_compare_two_products():
    """Debe comparar dos productos válidos correctamente"""
    res = client.get("/api/compare?ids=P001&ids=P002")
    assert res.status_code == 200
    data = res.json()
    assert data["count"] == 2
    assert "differences" in data
    assert "summary" in data
    assert "best_price" in data["summary"]
    assert "best_rating" in data["summary"]


def test_compare_multiple_products():
    """Debe permitir comparar más de dos productos"""
    res = client.get("/api/compare?ids=P001&ids=P002&ids=P003")
    assert res.status_code == 200
    data = res.json()
    assert data["count"] == 3
    assert "price" in data["differences"]
    assert "rating" in data["differences"]


def test_compare_requires_two_ids():
    """Debe devolver error 400 si se envía un solo ID"""
    res = client.get("/api/compare?ids=P001")
    assert res.status_code == 400
    data = res.json()
    assert "error" in data
    assert data["error"]["type"] in ["bad_request", "validation_error"]


# Test de validación y errores
def test_invalid_price_validation():
    """Debe devolver 422 si el parámetro min_price es negativo"""
    res = client.get("/api/products?min_price=-5")
    assert res.status_code == 422
    data = res.json()
    assert data["error"]["type"] == "validation_error"
    assert "details" in data


def test_internal_server_error(monkeypatch):
    """Simula un error inesperado y verifica respuesta 500"""
    def mock_broken_method(*args, **kwargs):
        raise Exception("Unexpected crash")

    monkeypatch.setattr("app.services.ProductService.list_products", mock_broken_method)

    res = client.get("/api/products")
    assert res.status_code == 500
    data = res.json()
    assert data["error"]["type"] == "internal_error"
    assert "Error interno" in data["error"]["message"]
