from extensions import db, cache
from models.product_m import Product
from repositories.invoice_repo import InvoiceRepo
from validators.invoice_validator import validate_invoice
from exceptions.api_exceptions import BadRequestError
from repositories.product_repo import ProductRepo

def return_purchase(invoice_number):
    invoice=InvoiceRepo.get_by_number(invoice_number)
    validate_invoice(invoice)
    purchase=invoice.purchase
    if purchase.status=="returned":
        raise BadRequestError("Purchase already returned.")
    for item in purchase.items:
        item.product.stock+=item.quantity
    purchase.status="returned"
    db.session.commit()
    cache.clear()
    return{"message": "Purchase returned successfully."}