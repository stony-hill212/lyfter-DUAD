from extensions import db
from models.address_m import Address

class AddressRepo:
    @staticmethod
    def add(address):
        db.session.add(address)
        db.session.commit()
        return address
    
    @staticmethod
    def add_to_session(address):
        db.session.add(address)
    
    @staticmethod
    def get_by_id(billing_address):
        return Address.query.get(billing_address)
    
    @staticmethod
    def get_user_addresses(user_id):
        return Address.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def delete(address):
        db.session.delete(address)
        db.session.commit()

    @staticmethod
    def commit():
        db.session.commit()

    @staticmethod
    def get_all():
        return Address.query.all()