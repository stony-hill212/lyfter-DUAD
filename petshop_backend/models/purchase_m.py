from extensions import db
from datetime import datetime

class Purchase(db.Model):
    __tablename__="purchases"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    billing_address=db.Column(db.Integer, db.ForeignKey("addresses.id"), nullable=False)
    address=db.relationship("Address", foreign_keys=[billing_address])
    payment_method=db.Column(db.String(50), nullable=False)
    total_amount=db.Column(db.Float, nullable=False)
    status=db.Column(db.String(20), nullable=False, default="completed")
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    items=db.relationship("PurchaseItem", backref="purchase", lazy=True, cascade="all, delete-orphan")
    invoice=db.relationship("Invoice", back_populates="purchase", uselist=False)