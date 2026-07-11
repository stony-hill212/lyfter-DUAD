from exceptions.api_exceptions import BadRequestError, NotFoundError

def validate_activate_cart(cart):
    if cart is None:
        raise NotFoundError("No active cart found.")

def validate_car_not_empty(cart):
    if not cart.items:
        raise BadRequestError("The cart is empty.")
    
def validate_payment(payment_method):
    allowed=["cash", "bank_transfer", "paypal"]
    if payment_method not in allowed:
        raise BadRequestError("Invalid payment method.")
    
def validate_checkout_stock(cart):
    for item in cart.items:
        if item.quantity>item.product.stock:
            raise BadRequestError(f"Not enough stock for '{item.product.name}'.")