from repositories.purchase_repo import PurchaseRepo
from schemas.purchase_schema import purchase_schema, purchases_schema
from exceptions.api_exceptions import NotFoundError

def get_all_purchases():
    purchases=PurchaseRepo.get_all()
    return purchases_schema.dump(purchases)

def get_purchase(purchase_id):
    purchase=PurchaseRepo.get_by_id(purchase_id)
    if not purchase:
        raise NotFoundError("Purchase not found.")
    return purchase_schema.dump(purchase)