from extensions import db
from models.purchase_m import Purchase
from models.purchaseItems import PurchaseItem

class PurchaseRepo:
    @staticmethod
    def create_purchase(purchase):
        db.session.add(purchase)
    
    @staticmethod
    def create_item(item):
        db.session.add(item)

    @staticmethod
    def commit():
        db.session.commit()
    
    @staticmethod
    def rollback():
        db.session.rollback()