from repositories.fruit_repo import FruitRepository
from repositories.invoice_repository import InvoiceRepository

class PurchaseService:
    @staticmethod
    def purchase(user_id, fruit_id, quantity):
        fruit=FruitRepository.get_by_id(fruit_id)
        if fruit is None:
            return None, "Fruit not found"
        if fruit.amount<quantity:
            return None, "Insufficient stock"
        subtotal=fruit.price*quantity
        invoice=InvoiceRepository.create_invoice(user_id, subtotal)
        InvoiceRepository.create_invoice_details(
            invoice.id,
            fruit.id,
            quantity,
            fruit.price,
            subtotal
        )
        fruit.amount-=quantity
        InvoiceRepository.commit()
        return invoice, None