from extensions import db
from models.purchase_m import Purchase
from models.purchaseItems import PurchaseItem
from repositories.purchase_repo import PurchaseRepo
from repositories.fruit_repo import FruitRepository

class PurchaseService:
    @staticmethod
    def create_purchase(items):
        try:
            purchase=Purchase()
            PurchaseRepo.create_purchase(purchase)
            db.session.flush()
            for item_data in items:
                fruit=FruitRepository.get_by_id(item_data["fruit_id"])
                if not fruit:
                    raise ValueError(f"Fruit {item_data['fruit_id']} not found")
                quantity=item_data["quantity"]
                if quantity<=0:
                    raise ValueError("Quantity must be greater than 0")
                if fruit.amount<quantity:
                    raise ValueError(f"Not enough stock for {fruit.name}")
                fruit.amount-=quantity
                purchase_item=PurchaseItem(
                    purchase_id=purchase.id,
                    fruit_id=fruit.id,
                    quantity=quantity
                )
                PurchaseRepo.create_item(purchase_item)
            PurchaseRepo.commit()
            return purchase
        except Exception:
            PurchaseRepo.rollback()
            raise
