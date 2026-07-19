from flask import Blueprint, jsonify
from extensions import cache
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from utils.decorators import admin_required
from services.invoice_s import get_invoice, get_all_invoices

invoice_bp=Blueprint("invoice",__name__)

@invoice_bp.route("/<string:invoice_number>",methods=["GET"])
@jwt_required()
def retrieve_invoice(invoice_number):
    user_id=get_jwt_identity()
    role=get_jwt()["role"]
    return jsonify(get_invoice(
        invoice_number,
        user_id,
        role
    )), 200

@invoice_bp.route("/",methods=["GET"])
@jwt_required()
@admin_required
@cache.cached()
def list_all():
    return jsonify(get_all_invoices()), 200