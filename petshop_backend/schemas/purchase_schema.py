from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields
from models.purchase_m import Purchase
from schemas.purchase_item_schema import PurchaseItemSchema
from schemas.address_schema import AddressSchema

class PurchaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Purchase
        load_instance=True

    id=auto_field()
    payment_method=auto_field()
    total_amount=auto_field()
    status=auto_field()
    created_at=auto_field()

    address=fields.Nested(AddressSchema)
    items=fields.Nested(PurchaseItemSchema, many=True)

purchase_schema=PurchaseItemSchema()
purchases_schema=PurchaseItemSchema(many=True)