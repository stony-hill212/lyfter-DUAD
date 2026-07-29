from extensions import db, cache
from repositories.cart_repo import CartRepo
from repositories.purchase_repo import PurchaseRepo
from repositories.product_repo import ProductRepo
from repositories.invoice_repo import InvoiceRepo
from repositories.purchase_item_repo import PurchaseItemRepo
from validators.purchase_validator import validate_activate_cart, validate_car_not_empty, validate_payment,validate_checkout_stock
from models.purchase_m import Purchase
from models.purchase_item_m import PurchaseItem
from models.invoice_m import Invoice
from utils.invoice_generator import generate_invoice_number
from schemas.invoice_schema import invoice_schema
from routes.invoice_r import retrieve_invoice, list_all

def checkout(user_id, billing_address, payment_method):
    cart=CartRepo.get_active_cart(user_id)
    validate_activate_cart(cart)
    validate_car_not_empty(cart)
    validate_payment(payment_method)
    validate_checkout_stock(cart)
    try:
        purchase=Purchase(
            user_id=user_id,
            billing_address=billing_address,
            payment_method=payment_method,
            status="completed",
            total_amount=0
        )
        PurchaseRepo.add_to_session(purchase)
        db.session.flush()
        purchase_total=0
        for item in cart.items:
            subtotal=item.quantity*item.product.price
            purchase_total+=subtotal
            purchase_item=PurchaseItem(
                purchase_id=purchase.id,
                product_id=item.product_id,
                quantity=item.quantity,
                unit_price=item.product.price,
                subtotal=subtotal
            )
            PurchaseItemRepo.add_to_session(purchase_item)
            item.product.stock-=item.quantity
        purchase.total_amount=purchase_total
        invoice=Invoice(invoice_number=generate_invoice_number(),purchase_id=purchase.id, total_amount=purchase.total_amount)
        InvoiceRepo.add_to_session(invoice)
        cart.status="completed"
        db.session.commit()
        cache.clear()
        return invoice_schema.dump(invoice)
    except Exception:
        db.session.rollback()
        raise