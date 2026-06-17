from extensions import db

class Contact(db.Model):
    __tablename__="contacts"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    phone=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(120), nullable=False)
    owner_id=db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)