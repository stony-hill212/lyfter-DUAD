from exceptions.api_exceptions import BadRequestError, NotFoundError

def validate_quantity(quantity):
    if quantity<=0:
        raise BadRequestError("Quantity must be greater than zero.")

def validate_stock(product, quantity):
    if quantity>product.stock:
        raise BadRequestError("Not enough items in stock.")
    
def validate_cart(cart):
    if not cart:
        raise NotFoundError("Cart not found.")

def validate_cart_item(cart_item):
    if not cart_item:
        raise NotFoundError("Item not found.")

def validate_product(product):
    if not product:
        raise NotFoundError("Product not found.")