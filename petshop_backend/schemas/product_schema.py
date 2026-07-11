from extensions import ma
from models.product_m import Product
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class ProductSchema(SQLAlchemySchema):

    class Meta:
        model=Product

    id=auto_field()
    name=auto_field()
    description=auto_field()
    price=auto_field()
    stock=auto_field()

product_schema=ProductSchema()
products_schema=ProductSchema(many=True)