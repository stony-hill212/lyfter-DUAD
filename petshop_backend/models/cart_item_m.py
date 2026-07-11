from extensions import db
from datetime import datetime

class CartItem(db.Model):
    __tablename__="cart_item"
    id=db.Column(db.Integer, primary_key=True)
    cart_id=db.Column(db.Integer, db.ForeignKey("carts.id"), nullable=False)
    product_id=db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)
    cart=db.relationship("Cart", back_populates="items")
    product=db.relationship("Product", back_populates="cart_items")
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)