from repositories.base_repository import BaseRepository
from models.product_m import Product

class ProductRepo(BaseRepository):
    model=Product
    @classmethod
    def exists(cls, product_id):
        return cls.get_by_id(product_id)is not None