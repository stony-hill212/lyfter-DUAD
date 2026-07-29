from flask import Blueprint, jsonify, request
from utils.decorators import admin_required
from services.user_s import get_all_users, get_user, update_user, delete_user

user_bp=Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("/",methods=["GET"])
@admin_required
def list_users():
    return jsonify(get_all_users()), 200

@user_bp.route("/<int:user_id>",methods=["GET"])
@admin_required
def retrieve_user(user_id):
    return jsonify(get_user(user_id)), 200

@user_bp.route("/<int:user_id>",methods=["PUT"])
@admin_required
def modify_user(user_id):
    data=request.get_json()
    return jsonify(update_user(user_id, data))

@user_bp.route("/<int:user_id>",methods=["DELETE"])
@admin_required
def remove_user(user_id):
    return jsonify(delete_user(user_id))