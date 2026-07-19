from extensions import db
from models.purchase_item_m import PurchaseItem

class PurchaseItemRepo:
    @staticmethod
    def add(item):
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def add_to_session(item):
        db.session.add(item)

    @staticmethod
    def commit():
        db.session.commit()