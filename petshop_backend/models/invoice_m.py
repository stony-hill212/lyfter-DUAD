from extensions import db
from datetime import datetime

class Invoice(db.Model):
    __tablename__="invoices"
    id=db.Column(db.Integer, primary_key=True)
    invoice_number=db.Column(db.String(50), nullable=False, unique=True)
    purchase_id=db.Column(db.Integer, db.ForeignKey("purchases.id"), nullable=False ,unique=True)
    total_amount=db.Column(db.Float, nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    purchase=db.relationship("Purchase", back_populates="invoice")