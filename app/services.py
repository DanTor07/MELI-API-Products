from app.repository import ProductRepository
from app.errors import ApiError

class ProductService:
    def __init__(self):
        self.repo = ProductRepository()

    def list_products(self, q, min_price, max_price, min_rating, sort_by, order, limit, offset):
        products = self.repo.find_all(q, min_price, max_price, min_rating, sort_by, order)
        total = len(products)
        return {"total": total, "items": products[offset: offset + limit]}

    def get_product(self, product_id: str):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ApiError.not_found(f"Producto '{product_id}' no encontrado")
        return product

    def compare_products(self, ids: list[str]):
        if not ids or len(ids) < 2:
            raise ApiError.bad_request("Debe enviar al menos dos IDs para comparar")

        products = [self.repo.get_by_id(pid) for pid in ids]
        missing = [pid for pid, p in zip(ids, products) if not p]
        if missing:
            raise ApiError.not_found(f"Producto(s) no encontrado(s): {', '.join(missing)}")

        products_data = [p.dict() for p in products]

        prices = [p["price"] for p in products_data]
        ratings = [p["rating"] for p in products_data]

        differences = {
            "price": {
                "min": min(prices),
                "max": max(prices),
                "range": round(max(prices) - min(prices), 2),
            },
            "rating": {
                "min": min(ratings),
                "max": max(ratings),
                "range": round(max(ratings) - min(ratings), 2),
            },
        }

        all_specs_keys = set().union(*[p["specifications"].keys() for p in products_data])
        specs_diff = {}

        for key in all_specs_keys:
            values = [p["specifications"].get(key) for p in products_data]
            if len(set(values)) > 1:  # solo si difieren
                specs_diff[key] = values

        differences["specs_diff"] = specs_diff


        best_price_product = min(products_data, key=lambda x: x["price"])["id"]
        best_rating_product = max(products_data, key=lambda x: x["rating"])["id"]

        summary = {
            "best_price": best_price_product,
            "best_rating": best_rating_product,
        }

        return {
            "count": len(products),
            "products": products_data,
            "differences": differences,
            "summary": summary,
        }
