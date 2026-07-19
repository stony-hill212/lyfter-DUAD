from repositories.address_repo import AddressRepo
from schemas.address_schema import address_schema, addresses_schema
from models.address_m import Address
from extensions import cache
from validators.address_validator import validate_required_fields

def create_address(user_id, data):
    validate_required_fields(data)
    address=Address(
        user_id=user_id,
        street=data["street"],
        city=data["city"],
        state=data.get("state"),
        country=data["country"],
        postal_code=data.get("postal_code")
    )
    AddressRepo.add(address)
    cache.clear()
    return address_schema.dump(address)

def get_addresses(user_id):
    addresses=AddressRepo.get_user_addresses(user_id)
    return addresses_schema.dump(addresses)

def get_all_addresses():
    addresses=AddressRepo.get_all()
    return addresses_schema.dump(addresses)