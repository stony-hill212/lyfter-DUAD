from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, create_refresh_token
from services.auth_service import AuthService
from services.login_history_service import LoginHistoryService
from utils.decorators import admin_required

auth_bp=Blueprint("auth", __name__)

@auth_bp.route("/register",methods=["POST"])
def register():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")
    user=AuthService.register(
        username,
        password
    )
    if user is None:
        return jsonify({"message": "Username already exist"}), 400
    token=create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    return jsonify({"token": token}), 201

@auth_bp.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")
    user=AuthService.login(username, password)
    if user is None:
        LoginHistoryService.log_attempt(
            user_id=None,
            ip_address=request.remote_addr or "127.0.1",
            success=False
        )
        return jsonify({"message": "Invalid credentials"}), 401
    token=create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    refresh_token=create_refresh_token(identity=str(user.id), additional_claims={"role": user.role})
    LoginHistoryService.log_attempt(
            user_id=user.id,
            ip_address=request.remote_addr or "127.0.1",
            success=True
        )
    return jsonify({
        "access_token": token,
        "refresh_token": refresh_token
    }), 200

@auth_bp.route("/refresh-token",methods=["POST"])
@jwt_required(refresh=True)
def refresh_token():
    identity=get_jwt_identity()
    claims=get_jwt()
    access_token=create_access_token(
        identity=identity,
        additional_claims={"role":claims.get("role")}
    )
    return jsonify({"access_token":access_token}), 200

@auth_bp.route("/login-history/<int:user_id>",methods=["GET"])
@jwt_required()
@admin_required
def get_login_history(user_id):
    history=LoginHistoryService.get_all(user_id)
    return jsonify([
        {
            "id":item.id,
            "user_id":item.user_id,
            "timestamp":item.timestamp.isoformat(),
            "ip_address":item.ip_address,
            "success":item.success
        }
        for item in history
    ]), 200

@auth_bp.route("/login-history",methods=["GET"])
@jwt_required()
@admin_required
def get_all_login_history():
    history=LoginHistoryService.get_all_info()
    return jsonify([
        {
            "id":item.id,
            "user_id":item.user_id,
            "timestamp":item.timestamp.isoformat(),
            "ip_address":item.ip_address,
            "success":item.success
        }
        for item in history
    ]), 200
