from exceptions.api_exceptions import NotFoundError

def validate_invoice(invoice):
    if invoice is None:
        raise NotFoundError("Invoice not found.")