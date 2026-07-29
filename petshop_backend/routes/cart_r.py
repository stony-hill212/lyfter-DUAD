from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.cart_s import add_product_to_cart, view_cart, update_quantity, remove_product

cart_bp=Blueprint("cart",__name__,url_prefix="/cart")

@cart_bp.route("/",methods=["GET"])
@jwt_required()
def get_cart():
    user_id=get_jwt_identity()
    return jsonify(view_cart(user_id))

@cart_bp.route("/add",methods=["POST"])
@jwt_required()
def add_to_cart():
    data=request.get_json()
    user_id=get_jwt_identity()
    result=add_product_to_cart(
        user_id,
        data["product_id"],
        data["quantity"]
    )
    return jsonify(result), 201

@cart_bp.route("/update",methods=["PUT"])
@jwt_required()
def update_cart_item():
    data=request.get_json()
    user_id=get_jwt_identity()
    result=update_quantity(
        user_id,
        data["product_id"],
        data["quantity"]
    )
    return jsonify(result)

@cart_bp.route("/remove/<int:product_id>",methods=["DELETE"])
@jwt_required()
def remove_item(product_id):
    user_id=get_jwt_identity()
    result=remove_product(user_id, product_id)
    return jsonify(result)