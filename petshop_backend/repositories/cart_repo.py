from repositories.base_repository import BaseRepository
from models.cart_m import Cart

class CartRepo(BaseRepository):
    model=Cart
    @classmethod
    def get_active_cart(cls, user_id):
        return cls.model.query.filter_by(user_id=user_id, status="active").first()