from models.user_m import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from exceptions.api_exceptions import UnauthorizedError, BadRequestError

def register_user(data):
    existing_user=User.query.filter(
        (
            User.username==data["username"]
        ) |
        (
            User.email==data["email"]
        )
    ).first()
    if existing_user:
        raise BadRequestError(
            "User already exists."
        )
    hashed_password=generate_password_hash(data["password"])
    new_user=User(
        username=data["username"],
        email=data["email"],
        password=hashed_password,
        role="user"
    )
    if new_user.role!="user":
        raise UnauthorizedError("Invalid role.")
    db.session.add(new_user)
    db.session.commit()
    return{"message": "User registered successfully"}

def login_user(data):
    user=User.query.filter_by(email=data["email"]).first()
    if not user:
        raise UnauthorizedError("Invalid credentials.")
    valid_password=check_password_hash(user.password, data["password"])
    if not valid_password:
        raise UnauthorizedError("Invalid credentials.")
    access_token=create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    return{
        "access_token": access_token,
        "user_id": user.id
    }