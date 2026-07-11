from repositories.invoice_repo import InvoiceRepo
from extensions import cache
from validators.invoice_validator import validate_invoice
from schemas.invoice_schema import invoice_schema, invoices_schema

def get_invoice(invoice_number):
    invoice=InvoiceRepo.get_by_number(invoice_number)
    validate_invoice(invoice)
    cache.delete(invoice_number)
    return invoice_schema.dump(invoice)

def get_all_invoices():
    invoices=InvoiceRepo.get_all()
    cache.delete("all_invoices")
    return invoices_schema.dump(invoices)