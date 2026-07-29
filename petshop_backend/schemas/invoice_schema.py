from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.invoice_m import Invoice
from schemas.address_summary_schema import AddressSummarySchema
from schemas.purchase_item_schema import PurchaseItemSchema
from schemas.address_schema import address_schema

class InvoiceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Invoice
        load_instance=True

    def get_billing_address(self, obj):
        if obj.purchase and obj.purchase.address:
            return address_schema.dump(obj.purchase.address)
        return None
    
    purchase_id=fields.Integer()
    total=fields.Float()
    invoice_number=fields.String()
    created_at=fields.DateTime()
    billing_address=fields.Method("get_billing_address")

invoice_schema=InvoiceSchema()
invoices_schema=InvoiceSchema(many=True)