from extensions import ma
from models.user_m import User
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=User
        load_instance=True

    id=auto_field()
    username=auto_field()
    email=auto_field()
    role=auto_field()
    created_at=auto_field()

user_schema=UserSchema()
users_schema=UserSchema(many=True)