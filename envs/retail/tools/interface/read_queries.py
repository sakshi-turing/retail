import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool

class ReadQueries(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        entity: str,
        entity_id: str
    ) -> str:
        store = data.get(entity, {})

        if entity_id not in store:
            return json.dumps({
                "error": f"{entity} with id {entity_id} not found"
            })

        return json.dumps(store[entity_id])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "read_queries",
                "description": "Read retail entities like supplier, product, orders, and shipping",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entity": {
                            "type": "string",
                            "enum": [
                                "supplier",
                                "product",
                                "purchase_order",
                                "sales_order",
                                "shipping"
                            ]
                        },
                        "entity_id": {
                            "type": "string"
                        }
                    },
                    "required": ["entity", "entity_id"]
                }
            }
        }
