from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.address_m import Address

class AddressSummarySchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Address
        load_instance=True
    
    street=auto_field()
    city=auto_field()
    country=auto_field()

address_summary_schema=AddressSummarySchema()