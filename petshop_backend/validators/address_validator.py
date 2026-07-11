from exceptions.api_exceptions import BadRequestError, NotFoundError

def validate_address(address):
    if address is None:
        raise NotFoundError("Address not found.")
    
def validate_required_fields(data):
    required=[
        "street",
        "city",
        "country"
    ]
    for field in required:
        if not data.get(field):
            raise BadRequestError(f"{field} is required.")