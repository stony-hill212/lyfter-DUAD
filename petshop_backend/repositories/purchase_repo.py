from extensions import db
from models.purchase_m import Purchase
from sqlalchemy.orm import joinedload
from repositories.base_repository import BaseRepository

class PurchaseRepo:
    @staticmethod
    def add(purchase):
        db.session.add(purchase)
        db.session.commit()
        return purchase
    
    @classmethod
    def get_by_id(cls, purchase_id):
        return(Purchase.query.options(
            joinedload(Purchase.items),
            joinedload(Purchase.address)
        ).filter_by(id=purchase_id).first())
    
    @staticmethod
    def get_by_user(user_id):
        return Purchase.query.filter_by(user_id=user_id).all()
    
    @classmethod
    def get_all(cls):
        return (Purchase.query.options(
            joinedload(Purchase.items),
            joinedload(Purchase.address)
        ).all())
    
    @staticmethod
    def commit():
        db.session.commit()
    
    @staticmethod
    def add_to_session(purchase):
        db.session.add(purchase)