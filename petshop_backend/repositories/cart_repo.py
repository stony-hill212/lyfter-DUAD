from repositories.base_repository import BaseRepository
from models.cart_m import Cart
from repositories.cart_item_repo import CartItem
from sqlalchemy.orm import joinedload

class CartRepo(BaseRepository):
    model=Cart
    @classmethod
    def get_active_cart(cls, user_id):
        return(
            cls.model.query.options(
                joinedload(Cart.items).joinedload(CartItem.product)
            ).filter_by(user_id=user_id, status="active").first()
        )