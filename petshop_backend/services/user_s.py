from repositories.user_repo import UserRepo
from schemas.user_schema import user_schema, users_schema
from exceptions.api_exceptions import NotFoundError
from validators.user_validator import validate_user, validate_role
from werkzeug.security import generate_password_hash

def get_all_users():
    users=UserRepo.get_all()
    return users_schema.dump(users)

def get_user(user_id):
    user=UserRepo.get_by_id(user_id)
    if not user:
        raise NotFoundError("User not found.")
    return user_schema.dump(user)

def update_user(user_id, data):
    user=UserRepo.get_by_id(user_id)
    validate_user(user)
    user.username=data.get("username", user.username)
    user.email=data.get("email",user.email)
    if "password" in data:
        user.password=generate_password_hash(data["password"])
    if "role" in data:
        validate_role(data["role"])
        user.role=data["role"]
    UserRepo.commit()
    return{"message": "User updated successfully."}

def delete_user(user_id):
    user=UserRepo.get_by_id(user_id)
    validate_user(user)
    UserRepo.delete(user)
    return{"message": "User deleted successfully."}