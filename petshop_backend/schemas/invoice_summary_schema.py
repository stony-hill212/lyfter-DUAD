from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.invoice_m import Invoice

class InvoiceSummarySchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Invoice
        load_instance=True
    
    invoice_number=auto_field()
    total=auto_field()
    created_at=auto_field()

invoice_summary_schema=InvoiceSummarySchema()