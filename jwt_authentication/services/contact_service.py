from models.contact import Contact
from repositories.contact_repo import ContactRepo

class ContactService:
    @staticmethod
    def create_contact(name, phone, email, owner_id):
        contact=Contact(
            name=name,
            phone=phone,
            email=email,
            owner_id=owner_id
        )
        return ContactRepo.create(contact)
    
    @staticmethod
    def get_contacts(user_id, role):
        if role=="ADMIN":
            return ContactRepo.get_all()
        return ContactRepo.get_by_owner(user_id)
    
    @staticmethod
    def update_contact(contact_id, data, user_id, role):
        contact=ContactRepo.get_by_id(contact_id)
        if not contact:
            return None
        if role!="ADMIN" and contact.owner_id!=user_id:
            return "FORBIDDEN"
        contact.name=data.get("name", contact.name)
        contact.phone=data.get("phone", contact.phone)
        contact.email=data.get("email", contact.email)
        ContactRepo.save()
        return contact
    
    @staticmethod
    def delete_contact(contact_id, user_id, role):
        contact=ContactRepo.get_by_id(contact_id)
        if not contact:
            return None
        if role!="ADMIN" and contact.owner_id!=user_id:
            return "FORBIDDEN"
        ContactRepo.delete(contact)
        return True