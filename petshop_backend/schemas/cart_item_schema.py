from extensions import ma
from models.cart_item_m import CartItem
from marshmallow import fields
from schemas.product_summary_schema import ProductSummarySchema

class CartItemSchema(ma.SQLAlchemyAutoSchema):
    product=fields.Nested(ProductSummarySchema)
    subtotal=fields.Method("get_subtotal")
    
    class Meta:
        model=CartItem
        load_instance=True
        include_fk=True

    def get_total(self, obj):
        return sum(
            item.quantity*item.product.price
            for item in obj.items
        )
    
    def get_subtotal(self, obj):
        return obj.quantity*obj.product.price
    
cart_item_schema=CartItemSchema()