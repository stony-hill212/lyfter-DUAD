from uuid import uuid4

def generate_invoice_number():
    """
    Generates a unique invoice number.
    Example:
    INV-7F4A2C91
    """
    return f"INV-{uuid4().hex[:8].upper()}"