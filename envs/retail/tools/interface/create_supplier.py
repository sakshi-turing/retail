import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool

class CreateSupplier(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        supplier_id: str,
        name: str,
        country: str
    ) -> str:
        suppliers = data.get("supplier", {})

        if supplier_id in suppliers:
            return json.dumps({"error": "Supplier already exists"})

        suppliers[supplier_id] = {
            "supplier_id": supplier_id,
            "name": name,
            "country": country
        }

        data["supplier"] = suppliers
        return json.dumps({"status": "CREATED", "supplier_id": supplier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_supplier",
                "description": "Create a new supplier",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "name": {"type": "string"},
                        "country": {"type": "string"}
                    },
                    "required": ["supplier_id", "name", "country"]
                }
            }
        }
