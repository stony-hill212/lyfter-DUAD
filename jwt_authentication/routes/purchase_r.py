from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.purchase_service import PurchaseService

purchase_bp=Blueprint("purchase",__name__)

@purchase_bp.route("/purchase",methods=["POST"])
@jwt_required()
def purchase():
    data=request.get_json()
    try:
        user_id=int(get_jwt_identity())
        invoice=PurchaseService.create_purchase(user_id, data["items"])
        return jsonify({
            "message": "Purchase completed",
            "invoice_id": invoice.id,
            "total": invoice.total
        }), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception:
        return jsonify({"message": "Purchase failed"}), 500
