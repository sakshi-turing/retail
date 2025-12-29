import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class CreateProduct(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        product_id: str,
        name: str,
        supplier_id: str,
        unit_price: float
    ) -> str:
        products = data.get("product", {})
        suppliers = data.get("supplier", {})

        if supplier_id not in suppliers:
            return json.dumps({"error": "Supplier does not exist"})

        if product_id in products:
            return json.dumps({"error": "Product already exists"})

        products[product_id] = {
            "product_id": product_id,
            "name": name,
            "supplier_id": supplier_id,
            "unit_price": unit_price
        }

        data["product"] = products
        return json.dumps({"status": "CREATED", "product_id": product_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_product",
                "description": "Create a new product",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "name": {"type": "string"},
                        "supplier_id": {"type": "string"},
                        "unit_price": {"type": "number"}
                    },
                    "required": ["product_id", "name", "supplier_id", "unit_price"]
                }
            }
        }
