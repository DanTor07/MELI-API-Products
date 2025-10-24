from pydantic import BaseModel, HttpUrl, Field
from typing import Dict, Any, List

class ProductOut(BaseModel):
    id: str
    product_name: str
    image_url: HttpUrl
    description: str
    price: float
    rating: float = Field(..., ge=0, le=5)
    specifications: Dict[str, Any]

class ProductsResponse(BaseModel):
    total: int
    items: List[ProductOut]
