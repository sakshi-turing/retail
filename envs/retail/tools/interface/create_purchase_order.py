import json
from typing import Any, Dict, List
from tau_bench.envs.tool import Tool

class CreatePurchaseOrder(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        purchase_order_id: str,
        supplier_id: str,
        items: List[Dict[str, Any]]
    ) -> str:
        """
        items example:
        [
          {"po_item_id": "POI001", "product_id": "PROD001", "quantity": 10, "unit_cost": 500}
        ]
        """

        suppliers = data.get("supplier", {})
        products = data.get("product", {})
        orders = data.get("purchase_order", {})
        order_items = data.get("purchase_order_item", {})

        # Validate supplier
        if supplier_id not in suppliers:
            return json.dumps({"error": "Supplier does not exist"})

        # Validate purchase order uniqueness
        if purchase_order_id in orders:
            return json.dumps({"error": "Purchase order already exists"})

        # Validate products
        for item in items:
            if item["product_id"] not in products:
                return json.dumps({
                    "error": f"Product {item['product_id']} does not exist"
                })

        # Create purchase order
        orders[purchase_order_id] = {
            "purchase_order_id": purchase_order_id,
            "supplier_id": supplier_id,
            "status": "CREATED"
        }

        # Create purchase order items
        for item in items:
            order_items[item["po_item_id"]] = {
                "po_item_id": item["po_item_id"],
                "purchase_order_id": purchase_order_id,
                "product_id": item["product_id"],
                "quantity": item["quantity"],
                "unit_cost": item["unit_cost"]
            }

        data["purchase_order"] = orders
        data["purchase_order_item"] = order_items

        return json.dumps({
            "status": "CREATED",
            "purchase_order_id": purchase_order_id,
            "item_count": len(items)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_purchase_order",
                "description": "Create a purchase order for a supplier with order items",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "purchase_order_id": {"type": "string"},
                        "supplier_id": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "po_item_id": {"type": "string"},
                                    "product_id": {"type": "string"},
                                    "quantity": {"type": "number"},
                                    "unit_cost": {"type": "number"}
                                },
                                "required": [
                                    "po_item_id",
                                    "product_id",
                                    "quantity",
                                    "unit_cost"
                                ]
                            }
                        }
                    },
                    "required": ["purchase_order_id", "supplier_id", "items"]
                }
            }
        }
