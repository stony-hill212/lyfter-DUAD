from extensions import db

class Fruit(db.Model):
    __tablename__="fruits"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    price=db.Column(db.Float, nullable=False)
    arrival_date=db.Column(db.Date, nullable=False)
    amount=db.Column(db.Integer, nullable=False)
    purchase_items=db.relationship("PurchaseItem", backref="fruit", lazy=True)
    def to_dict(self):
        return{
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "arrival_date":self.arrival_date,
            "amount":self.amount
        }
