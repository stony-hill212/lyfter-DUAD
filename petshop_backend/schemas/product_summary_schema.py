from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.product_m import Product
from marshmallow import fields

class ProductSummarySchema(SQLAlchemySchema):
    class Meta:
        model=Product

    id=auto_field()
    name=auto_field()
    price=auto_field()

product_summary_schema=ProductSummarySchema()
products_summary_schema=ProductSummarySchema()