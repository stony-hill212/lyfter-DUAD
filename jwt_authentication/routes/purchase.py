from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.purchase_service import PurchaseService

purchase_bp=Blueprint("purchase",__name__)

@purchase_bp.route("/purchases",methods=["POST"])
@jwt_required()
def purchase():
    data=request.get_json()
    fruit_id=data.get("fruit_id")
    quantity=data.get("quantity")
    user_id=get_jwt_identity()
    invoice,error=PurchaseService.purchase(int(user_id), fruit_id, quantity)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({
        "message": "Purchase completed",
        "invoice": invoice.to_dict()
    }), 201