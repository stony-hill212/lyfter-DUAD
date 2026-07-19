from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), nullable=False, unique=True)
    email=db.Column(db.String(120), nullable=False, unique=True)
    password=db.Column(db.String(255), nullable=False)
    role=db.Column(db.String(20), nullable=False, default="user")
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    addresses=db.relationship("Address", backref="user", lazy=True)
    carts=db.relationship("Cart", backref="user", lazy=True)
    purchases=db.relationship("Purchase", backref="user", lazy=True)