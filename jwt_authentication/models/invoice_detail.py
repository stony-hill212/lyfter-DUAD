from extensions import db

class InvoiceDetail(db.Model):
    __tablename__="invoice_details"
    id=db.Column(db.Integer, primary_key=True)
    invoice_id=db.Column(db.Integer, db.ForeignKey("invoices.id"), nullable=False)
    fruit_id=db.Column(db.Integer, db.ForeignKey("fruits.id"), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)
    unit_price=db.Column(db.Float, nullable=False)
    subtotal=db.Column(db.Float, nullable=False)

    def to_dict(self):
        return{
            "id":self.id,
            "invoice_id":self.invoice_id,
            "fruit_id":self.fruit_id,
            "quantity":self.quantity,
            "unit_price":self.unit_price,
            "subtotal":self.subtotal
        }