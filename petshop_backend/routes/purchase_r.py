from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.purchase_s import checkout

purchase_bp=Blueprint("purchase",__name__,url_prefix="/purchases")

@purchase_bp.route("/checkout", methods=["POST"])
@jwt_required()
def completed_completed():
    data=request.get_json()
    user_id=get_jwt_identity()
    result=checkout(
        user_id=user_id,
        billing_address=data["billing_address"],
        payment_method=data["payment_method"]
    )
    return jsonify(result), 201