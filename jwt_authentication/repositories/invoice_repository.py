from extensions import db
from models.invoice import Invoice
from models.invoice_detail import InvoiceDetail

class InvoiceRepository:
    @staticmethod
    def create_invoice(user_id, total):
        invoice=Invoice(user_id=user_id, total=total)
        db.session.add(invoice)
        db.session.flush()
        return invoice
    
    @staticmethod
    def create_invoice_details(
        invoice_id,
        fruit_id,
        quantity,
        unit_price,
        subtotal
    ):
        details=InvoiceDetail(
            invoice_id=invoice_id,
            fruit_id=fruit_id,
            quantity=quantity,
            unit_price=unit_price,
            subtotal=subtotal
        )
        db.session.add(details)
        return details
    
    @staticmethod
    def commit():
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id):
        return Invoice.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_all():
        return Invoice.query.all()
    
    @staticmethod
    def get_by_id(invoice_id):
        return Invoice.query.get(invoice_id)
    
    @staticmethod
    def get_details(invoice_id):
        return InvoiceDetail.query.filter_by(invoice_id=invoice_id).all()