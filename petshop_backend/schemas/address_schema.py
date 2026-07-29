from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.address_m import Address

class AddressSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Address
        load_instance=True
    
    id=auto_field()
    street=auto_field()
    city=auto_field()
    state=auto_field()
    country=auto_field()
    postal_code=auto_field()

address_schema=AddressSchema()
addresses_schema=AddressSchema(many=True)