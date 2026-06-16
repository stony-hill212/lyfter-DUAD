from extensions import db
from repositories.fruit_repo import FruitRepository
from repositories.invoice_repository import InvoiceRepository

class PurchaseService:
    @staticmethod
    def create_purchase(user_id, items):
        try:
            invoice=InvoiceRepository.create_invoice(
                user_id=user_id,
                total=0
            )
            total=0
            for item_data in items:
                fruit=FruitRepository.get_by_id(item_data["fruit_id"])
                if not fruit:
                    raise ValueError(f"Fruit {item_data['fruit_id']} not found")
                quantity=item_data["quantity"]
                if quantity<=0:
                    raise ValueError("Quantity must be greater than 0")
                if fruit.amount<quantity:
                    raise ValueError(f"Not enough stock for {fruit.name}")
                subtotal=fruit.price*quantity
                total+=subtotal
                fruit.amount-=quantity
                InvoiceRepository.create_invoice_details(
                    invoice.id,
                    fruit.id,
                    quantity,
                    fruit.price,
                    subtotal
                )
            invoice.total=total
            InvoiceRepository.commit()
            return invoice
        except Exception:
            InvoiceRepository.rollback()
            raise
