from repositories.invoice_repo import InvoiceRepo
from repositories.user_repo import UserRepo
from extensions import cache
from validators.invoice_validator import validate_invoice, validate_invoice_owner
from schemas.invoice_schema import invoice_schema, invoices_schema

def get_invoice(invoice_number, user_id, role):
    invoice=InvoiceRepo.get_by_number(invoice_number)
    validate_invoice(invoice)
    validate_invoice_owner(invoice, user_id, role)
    return invoice_schema.dump(invoice)

def get_all_invoices():
    invoices=InvoiceRepo.get_all()
    return invoices_schema.dump(invoices)