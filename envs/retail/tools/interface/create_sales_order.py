import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool

class CreateSalesOrder(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        sales_order_id: str,
        user_id: str,
        payment_method: str
    ) -> str:
        orders = data.get("sales_order", {})
        users = data.get("user", {})

        if user_id not in users:
            return json.dumps({"error": "User does not exist"})

        if sales_order_id in orders:
            return json.dumps({"error": "Sales order already exists"})

        orders[sales_order_id] = {
            "sales_order_id": sales_order_id,
            "user_id": user_id,
            "status": "PLACED",
            "payment_method": payment_method
        }

        data["sales_order"] = orders
        return json.dumps({"status": "PLACED", "sales_order_id": sales_order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_sales_order",
                "description": "Create a sales order for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sales_order_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "payment_method": {"type": "string"}
                    },
                    "required": ["sales_order_id", "user_id", "payment_method"]
                }
            }
        }
