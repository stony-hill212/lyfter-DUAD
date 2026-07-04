from extensions import db
from models.contact import Contact

class ContactRepo:
    @staticmethod
    def create(contact):
        db.session.add(contact)
        db.session.commit()
        return contact
    
    @staticmethod
    def get_by_id(contact_id):
        return Contact.query.get(contact_id)
    
    @staticmethod
    def get_all():
        return Contact.query.all()
    
    @staticmethod
    def get_by_owner(owner_id):
        return Contact.query.filter_by(owner_id=owner_id).all()
    
    @staticmethod
    def save():
        db.session.commit()
    
    @staticmethod
    def delete(contact):
        db.session.delete(contact)
        db.session.commit()