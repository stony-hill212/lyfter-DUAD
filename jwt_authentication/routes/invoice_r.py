from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from services.invoice_service import InvoiceService

invoice_bp=Blueprint("invoice",__name__)

@invoice_bp.route("/invoices",methods=["GET"])
@jwt_required()
def get_invoices():
    user_id=int(get_jwt_identity())
    role=get_jwt().get("role")
    invoices=InvoiceService.get_invoices(user_id, role)
    return jsonify([invoice.to_dict()for invoice in invoices]), 200

@invoice_bp.route("/invoices/<int:invoice_id>",methods=["GET"])
@jwt_required()
def get_invoice(invoice_id):
    user_id=int(get_jwt_identity())
    role=get_jwt().get("role")
    result,error=InvoiceService.get_invoice(invoice_id, user_id, role)
    if error:
        status=(
            404
            if error=="Invoice not found"
            else 403
        )
        return jsonify({"message": error}), status
    return jsonify(result), 200