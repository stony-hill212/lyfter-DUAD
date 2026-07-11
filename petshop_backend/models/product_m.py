from extensions import db
from datetime import datetime

class Product(db.Model):
    __tablename__="products"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    description=db.Column(db.Text)
    price=db.Column(db.Float, nullable=False)
    cart_items=db.relationship("CartItem", back_populates="product")
    stock=db.Column(db.Integer, nullable=False, default=0)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)