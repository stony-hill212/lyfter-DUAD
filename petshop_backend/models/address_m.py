from extensions import db
from datetime import datetime

class Address(db.Model):
    __tablename__="addresses"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    street=db.Column(db.String(100), nullable=False)
    city=db.Column(db.String(100), nullable=False)
    state=db.Column(db.String(100), nullable=False)
    country=db.Column(db.String(100), nullable=False)
    postal_code=db.Column(db.String(20), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)