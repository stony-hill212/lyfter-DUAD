from flask import Blueprint, jsonify
from utils.decorators import admin_required
from services.purchase_query_s import get_all_purchases, get_purchase

purchase_query_bp=Blueprint("purchase_query",__name__,url_prefix="/purchase-history")

@purchase_query_bp.route("/", methods=["GET"])
@admin_required
def list_purchases():
    return jsonify(get_all_purchases()), 200

@purchase_query_bp.route("/<int:purchase_id>",methods=["GET"])
@admin_required
def retrieve_purchase(purchase_id):
    return jsonify(get_purchase(purchase_id)), 200