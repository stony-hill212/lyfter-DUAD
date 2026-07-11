from extensions import db
from models.purchase_m import Purchase

class PurchaseRepo:
    @staticmethod
    def add(purchase):
        db.session.add(purchase)
        db.session.commit()
        return purchase
    
    @staticmethod
    def get_by_id(purchase_id):
        return Purchase.query.get(purchase_id)
    
    @staticmethod
    def get_by_user(user_id):
        return Purchase.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_all():
        return Purchase.query.all()
    
    @staticmethod
    def commit():
        db.session.commit()
    
    @staticmethod
    def add_to_session(purchase):
        db.session.add(purchase)