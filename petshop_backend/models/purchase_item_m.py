from extensions import db
from datetime import datetime

class PurchaseItem(db.Model):
    __tablename__="purchase_items"
    id=db.Column(db.Integer, primary_key=True)
    purchase_id=db.Column(db.Integer, db.ForeignKey("purchases.id"), nullable=False)
    product_id=db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)
    unit_price=db.Column(db.Float, nullable=False)
    subtotal=db.Column(db.Float, nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    product=db.relationship("Product", back_populates="purchase_items")