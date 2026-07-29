from extensions import ma
from models.cart_m import Cart
from marshmallow import fields
from schemas.cart_item_schema import CartItemSchema

class CartSchema(ma.SQLAlchemyAutoSchema):
    items=fields.Nested(CartItemSchema, many=True)
    class Meta:
        model=Cart
        load_instance=True
        include_fk=True