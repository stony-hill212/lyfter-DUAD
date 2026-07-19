from exceptions.api_exceptions import NotFoundError, ForbiddenError

def validate_invoice(invoice):
    if invoice is None:
        raise NotFoundError("Invoice not found.")

def validate_invoice_owner(invoice, user_id, role):
    if role=="admin":
        return
    if invoice.purchase.user_id!=int(user_id):
        raise ForbiddenError("Access not allowed.")