from extensions import db
from models.invoice_m import Invoice

class InvoiceRepo:
    @staticmethod
    def add(invoice):
        db.session.add(invoice)
        db.session.commit()
        return invoice
    
    @staticmethod
    def get_by_number(invoice_number):
        return Invoice.query.filter_by(invoice_number=invoice_number).first()
    
    @staticmethod
    def get_all():
        return Invoice.query.all()
    
    @staticmethod
    def commit():
        db.session.commit()
    
    @staticmethod
    def add_to_session(purchase):
        db.session.add(purchase)

    @staticmethod
    def get_by_user(invoice_number):
        return Invoice.query.filter_by(invoice_number=invoice_number).first()
    
    @staticmethod
    def get_all():
        return Invoice.query.all()