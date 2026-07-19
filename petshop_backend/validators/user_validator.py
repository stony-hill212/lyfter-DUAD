from exceptions.api_exceptions import NotFoundError, BadRequestError

def validate_user(user):
    if user is None:
        raise NotFoundError("User not found.")

def validate_role(role):
    allowed_roles=["admin", "user"]
    if role not in allowed_roles:
        raise BadRequestError("Invalid role.")