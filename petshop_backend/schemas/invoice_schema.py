from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.invoice_m import Invoice
from schemas.address_summary_schema import AddressSummarySchema
from schemas.purchase_item_schema import PurchaseItemSchema

class InvoiceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Invoice
        load_instance=True
    
    purchase_id=fields.Integer()
    total=fields.Float()
    invoice_number=fields.String()
    created_at=fields.DateTime()
    billing_address=fields.Nested(AddressSummarySchema, many=True)

invoice_schema=InvoiceSchema()
invoices_schema=InvoiceSchema(many=True)