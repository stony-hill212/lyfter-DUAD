from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.decorators import admin_required
from services.return_s import return_purchase

return_bp=Blueprint("return",__name__)

@return_bp.route("/<string:invoice_number>",methods=["POST"])
@jwt_required()
def make_return(invoice_number):
    return jsonify(return_purchase(invoice_number))