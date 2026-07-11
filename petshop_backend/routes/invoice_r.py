from flask import Blueprint, jsonify
from extensions import cache
from flask_jwt_extended import jwt_required
from utils.decorators import admin_required
from services.invoice_s import get_invoice, get_all_invoices

invoice_bp=Blueprint("invoice",__name__)

@invoice_bp.route("/<string:invoice_number>",methods=["GET"])
@jwt_required()
@cache.cached(timeout=300)
def retrieve_invoice(invoice_number):
    return jsonify(get_invoice(invoice_number)), 200

@invoice_bp.route("/",methods=["GET"])
@jwt_required()
@admin_required
@cache.cached()
def list_all():
    return jsonify(get_all_invoices()), 200