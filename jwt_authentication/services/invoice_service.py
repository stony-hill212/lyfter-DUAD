from repositories.invoice_repository import InvoiceRepository

class InvoiceService:
    @staticmethod
    def get_invoices(user_id, role):
        if role=="ADMIN":
            return InvoiceRepository.get_all()
        return InvoiceRepository.get_by_user_id(user_id)
    
    @staticmethod
    def get_invoice(invoice_id, user_id, role):
        invoice=InvoiceRepository.get_by_id(invoice_id)
        if invoice is None:
            return None, "Invoice not found"
        if (role!="ADMIN" and invoice.user_id!=user_id):
            return None, "Unauthorized"
        details=InvoiceRepository.get_details(invoice_id)
        return{
            "invoice": invoice.to_dict(),
            "details":[detail.to_dict()for detail in details]
        }, None