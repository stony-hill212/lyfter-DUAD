from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from services.auth_service import AuthService

me_bp=Blueprint("me",__name__)

@me_bp.route("/me",methods=["GET"])
@jwt_required()
def me():
    user_id=get_jwt_identity()
    user=AuthService.get_user_by_id(int(user_id))
    if user is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify({
        "id":user.id,
        "username":user.username
    }), 200