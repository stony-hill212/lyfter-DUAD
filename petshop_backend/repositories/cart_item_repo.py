from repositories.base_repository import BaseRepository
from models.cart_item_m import CartItem

class CartItemRepo(BaseRepository):
    model=CartItem
    @classmethod
    def get_cart_product(cls, cart_id, product_id):
        return CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()