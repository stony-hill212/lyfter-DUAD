from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token


from services.auth_service import AuthService

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
        return jsonify({"message": "Invalid credentials"}), 401
    token=create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    return jsonify({"token": token}), 200