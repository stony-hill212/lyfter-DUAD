from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.decorators import admin_required
from extensions import cache
from services.address_s import create_address, get_addresses, get_all_addresses

address_bp=Blueprint("addresses",__name__)

@address_bp.route("/",methods=["POST"])
@jwt_required()
def add_address():
    user_id=get_jwt_identity()
    result=create_address(user_id, request.get_json())
    return jsonify(result), 201

@address_bp.route("/",methods=["GET"])
@jwt_required()
@cache.cached()
def list_addresses():
    user_id=get_jwt_identity()
    return jsonify(get_addresses(user_id))

@address_bp.route("/show",methods=["GET"])
@jwt_required()
@admin_required
def list_all():
    return jsonify(get_all_addresses())