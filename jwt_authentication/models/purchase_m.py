from extensions import db
from datetime import datetime

class Purchase(db.Model):
    __tablename__="purchases"
    id=db.Column(db.Integer, primary_key=True)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    items=db.relationship("PurchaseItem", backref="purchase", lazy=True, cascade="all, delete-orphan")