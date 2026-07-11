from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields
from models.purchase_item_m import PurchaseItem
from schemas.product_summary_schema import ProductSummarySchema

class PurchaseItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=PurchaseItem
        load_instance=True

    id=auto_field()
    quantity=auto_field()
    unit_price=auto_field()
    subtotal=auto_field()
    product=fields.Nested(ProductSummarySchema)

purchase_item_schema=PurchaseItemSchema()
purchase_items_schema=PurchaseItemSchema()