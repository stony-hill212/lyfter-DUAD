from extensions import db
from datetime import datetime

class Cart(db.Model):
    __tablename__="carts"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status=db.Column(db.String(20), nullable=False, default="active")
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    items=db.relationship("CartItem", back_populates="cart", lazy=True, cascade="all, delete-orphan")