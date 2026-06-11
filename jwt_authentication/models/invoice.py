from extensions import db
from datetime import datetime

class Invoice(db.Model):
    __tablename__="invoices"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"),nullable=False)
    purchase_date=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total=db.Column(db.Float, nullable=False)

    def to_dict(self):
        return{
            "id":self.id,
            "user_id":self.user_id,
            "purchase_date":self.purchase_date.isoformat(),
            "total":self.total
        }