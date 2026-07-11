from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields
from models.cart_m import Cart
from schemas.cart_item_schema import CartItemSchema

class CartSummarySchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Cart
    id=auto_field()
    status=auto_field()
    created_at=auto_field()
    updated_at=auto_field()
    items=fields.Nested(CartItemSchema, many=True)
cart_summary_schema=CartSummarySchema()