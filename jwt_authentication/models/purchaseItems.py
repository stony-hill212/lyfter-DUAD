from extensions import db

class PurchaseItem(db.Model):
    __tablename__="purchase_items"
    id=db.Column(db.Integer, primary_key=True)
    purchase_id=db.Column(db.Integer, db.ForeignKey("purchases.id"), nullable=False)
    fruit_id=db.Column(db.Integer, db.ForeignKey("fruits.id"), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)