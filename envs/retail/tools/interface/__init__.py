from .create_supplier import CreateSupplier
from .create_product import CreateProduct
from .create_sales_order import CreateSalesOrder
from .update_order_status import UpdateOrderStatus
from .ship_order import ShipOrder
from .create_purchase_order import CreatePurchaseOrder
from .read_queries import ReadQueries

ALL_TOOLS_INTERFACE_1 = [
    CreateSupplier,
    CreateProduct,
    CreateSalesOrder,
    UpdateOrderStatus,
    ShipOrder,
    CreatePurchaseOrder,
    ReadQueries
]
