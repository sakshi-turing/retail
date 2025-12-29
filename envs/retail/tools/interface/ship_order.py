import json
from typing import Any, Dict
# from tau_bench.envs.tool import Tool
from retail.tools import Tool

class ShipOrder(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        shipping_id: str,
        sales_order_id: str,
        method: str,
        tracking_number: str
    ) -> str:
        orders = data.get("sales_order", {})
        shipping = data.get("shipping", {})

        if sales_order_id not in orders:
            return json.dumps({"error": "Sales order not found"})

        if orders[sales_order_id]["status"] != "PLACED":
            return json.dumps({"error": "Order not eligible for shipping"})

        shipping[shipping_id] = {
            "shipping_id": shipping_id,
            "sales_order_id": sales_order_id,
            "method": method,
            "tracking_number": tracking_number,
            "status": "SHIPPED"
        }

        orders[sales_order_id]["status"] = "SHIPPED"

        data["shipping"] = shipping
        data["sales_order"] = orders

        return json.dumps({
            "status": "SHIPPED",
            "sales_order_id": sales_order_id,
            "shipping_id": shipping_id
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ship_order",
                "description": "Ship a sales order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipping_id": {"type": "string"},
                        "sales_order_id": {"type": "string"},
                        "method": {"type": "string"},
                        "tracking_number": {"type": "string"}
                    },
                    "required": [
                        "shipping_id",
                        "sales_order_id",
                        "method",
                        "tracking_number"
                    ]
                }
            }
        }
