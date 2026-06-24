from flask import Blueprint, request, jsonify
from datetime import datetime
from extensions import db
from models.fruit import Fruit
from services.fruit_service import FruitService
from flask_jwt_extended import jwt_required
from utils.decorators import admin_required

fruit_bp=Blueprint("fruit",__name__)

@fruit_bp.route("/fruits",methods=["POST"])
@jwt_required()
@admin_required
def create_fruit():
    data=request.get_json()
    fruit=FruitService.create_fruit(data)
    if isinstance(fruit, dict)and "error" in fruit:
        return jsonify(fruit), 400
    return jsonify(fruit.to_dict()), 201

@fruit_bp.route("/fruits",methods=["GET"])
@jwt_required()
def get_fruits():
    fruits=FruitService.get_all_fruits()
    return jsonify(fruits), 200

@fruit_bp.route("/fruits/<int:fruit_id>",methods=["GET"])
@jwt_required()
def get_item(fruit_id):
    fruit=FruitService.get_fruit_by_id(fruit_id)
    if not fruit:
        return jsonify({"message": "Fruit not found"}), 404
    return jsonify(fruit), 200

@fruit_bp.route("/fruits/<int:fruit_id>",methods=["PUT"])
@jwt_required()
@admin_required
def update_fruit(fruit_id):
    data=request.get_json()
    fruit=FruitService.update_fruit(fruit_id, data)
    if not fruit:
        return jsonify({"message": "Fruit not found"}), 404
    return jsonify(fruit.to_dict()), 200

@fruit_bp.route("/fruits/<int:fruit_id>",methods=["DELETE"])
@jwt_required()
@admin_required
def delete_fruit(fruit_id):
    deleted=FruitService.delete_fruit(fruit_id)
    if not deleted:
        return jsonify({"message": "Fruit not found"}), 404
    return jsonify({"message": "Fruit deleted successfully"}), 200
