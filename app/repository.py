import json, os
from app.models import ProductOut

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "products.json")

class ProductRepository:
    def __init__(self, path: str = DATA_PATH):
        self.path = path
        self._cache = None

    def _load(self):
        if self._cache is None:
            with open(self.path, 'r', encoding='utf-8') as f:
                self._cache = json.load(f)
        return self._cache

    def get_by_id(self, product_id: str):
        for p in self._load():
            if p["id"] == product_id:
                return ProductOut(**p)
        return None

    def find_all(self, q, min_price, max_price, min_rating, sort_by, order):
        items = [ProductOut(**p) for p in self._load()]
        if q:
            items = [p for p in items if q.lower() in p.product_name.lower() or q.lower() in p.description.lower()]
        if min_price:
            items = [p for p in items if p.price >= min_price]
        if max_price:
            items = [p for p in items if p.price <= max_price]
        if min_rating:
            items = [p for p in items if p.rating >= min_rating]
        if sort_by:
            reverse = order == "desc"
            items.sort(key=lambda p: getattr(p, sort_by), reverse=reverse)
        return items
