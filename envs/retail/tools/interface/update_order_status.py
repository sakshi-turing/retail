import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool

class UpdateOrderStatus(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        sales_order_id: str,
        new_status: str
    ) -> str:
        orders = data.get("sales_order", {})

        if sales_order_id not in orders:
            return json.dumps({"error": "Sales order not found"})

        orders[sales_order_id]["status"] = new_status
        data["sales_order"] = orders

        return json.dumps({
            "status": "UPDATED",
            "sales_order_id": sales_order_id,
            "new_status": new_status
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order_status",
                "description": "Update sales order status",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sales_order_id": {"type": "string"},
                        "new_status": {"type": "string"}
                    },
                    "required": ["sales_order_id", "new_status"]
                }
            }
        }
