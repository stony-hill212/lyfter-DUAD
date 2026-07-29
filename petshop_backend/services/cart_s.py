from repositories.cart_repo import CartRepo
from repositories.cart_item_repo import CartItemRepo
from repositories.product_repo import ProductRepo
from models.cart_m import Cart
from models.cart_item_m import CartItem
from exceptions.api_exceptions import NotFoundError, BadRequestError
from schemas.cart_summary_schema import cart_summary_schema
from schemas.cart_item_schema import cart_item_schema
from validators.cart_validator import validate_cart, validate_cart_item, validate_quantity, validate_product, validate_stock

def get_or_create_cart(user_id):
    existing_cart=CartRepo.get_active_cart(user_id)
    if existing_cart:
        return existing_cart
    new_cart=Cart(user_id=user_id, status="active")
    CartRepo.add(new_cart)
    return new_cart

def get_cart_item(user_id, product_id):
    cart=get_or_create_cart(user_id)
    product=ProductRepo.get_by_id(product_id)
    validate_product(product)
    cart_item=CartItemRepo.get_cart_product(cart.id, product.id)
    validate_cart_item(cart_item)
    return cart, product, cart_item

def add_product_to_cart(user_id, product_id, quantity):
    product=ProductRepo.get_by_id(product_id)
    cart=get_or_create_cart(user_id)
    validate_product(product)
    validate_quantity(quantity)
    validate_stock(product, quantity)
    cart_item=CartItemRepo.get_cart_product(cart.id, product.id)
    if cart_item:
        new_quantity=cart_item.quantity+quantity
        validate_stock(product, new_quantity)
        cart_item.quantity=new_quantity
        CartItemRepo.commit()
    else:
        cart_item=CartItem(cart_id=cart.id, product_id=product.id, quantity=quantity)
        CartItemRepo.add(cart_item)
    return cart_summary_schema.dump(cart)

def view_cart(user_id):
    cart=CartRepo.get_active_cart(user_id)
    if not cart:
        raise NotFoundError("No active cart found.")
    return cart_summary_schema.dump(cart)

def update_quantity(user_id, product_id, quantity):
    cart,product,cart_item=get_cart_item(user_id, product_id)
    validate_quantity(quantity)
    validate_stock(product, quantity)
    cart_item.quantity=quantity
    CartItemRepo.commit()
    return cart_summary_schema.dump(cart)

def remove_product(user_id, product_id):
    cart,product,cart_item=get_cart_item(user_id, product_id)
    CartItemRepo.delete(cart_item)
    return{"message": "Product removed successfully"}