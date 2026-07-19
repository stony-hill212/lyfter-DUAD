from flask import Blueprint, request, jsonify
from services.auth_s import register_user, login_user
from utils.decorators import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

auth_bp=Blueprint("auth",__name__)

@auth_bp.route("/register",methods=["POST"])
def register():
    result=register_user(request.json)
    return jsonify(result), 201
    
@auth_bp.route("/login",methods=["POST"])
def login():
    result=login_user(request.json)
    return jsonify(result), 200
    
@auth_bp.route("/profile",methods=["GET"])
@jwt_required()
def profile():
    return jsonify({
        "user_id": get_jwt_identity(),
        "role": get_jwt()["role"]
    }), 200