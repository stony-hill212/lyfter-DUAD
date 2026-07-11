from extensions import cache
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from utils.decorators import admin_required
from services.product_s import create_product, get_all_products, get_product, update_products, delete_product

product_bp=Blueprint("products",__name__)

@product_bp.route("/",methods=["POST"])
@admin_required
def create():
    result=create_product(request.json)
    return jsonify(result), 201

@product_bp.route("/",methods=["GET"])
@jwt_required()
@cache.cached()
def get_all():
    return jsonify(get_all_products()), 200

@product_bp.route("/<int:product_id>",methods=["GET"])
@jwt_required()
@cache.memoize(timeout=60)
def get_item(product_id):
    return jsonify(get_product(product_id)), 200

@product_bp.route("/<int:product_id>",methods=["PUT"])
@admin_required
def update(product_id):
    result=update_products(product_id, request.json)
    return jsonify(result), 200

@product_bp.route("/<int:product_id>",methods=["DELETE"])
@admin_required
def delete(product_id):
    result=delete_product(product_id)
    return jsonify(result), 200