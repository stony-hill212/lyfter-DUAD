from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from services.contact_service import ContactService

contact_bp=Blueprint("contacts",__name__)

@contact_bp.route("/contacts",methods=["POST"])
@jwt_required()
def create_contact():
    data=request.get_json()
    user_id=int(get_jwt_identity())
    contact=ContactService.create_contact(
        data["name"],
        data["phone"],
        data["email"],
        user_id
    )
    return jsonify({
        "id":contact.id,
        "name":contact.name,
        "phone":contact.phone,
        "email":contact.email,
        "owner_id":contact.owner_id
    }), 201

@contact_bp.route("/contacts",methods=["GET"])
@jwt_required()
def get_contacts():
    user_id=int(get_jwt_identity())
    role=get_jwt().get("role")
    contacts=ContactService.get_contacts(user_id, role)
    return jsonify([
        {
            "id":c.id,
            "name":c.name,
            "phone":c.phone,
            "email":c.email,
            "owner_id":c.owner_id
        }
        for c in contacts
    ]), 200

@contact_bp.route("/contacts/<int:contact_id>",methods=["PUT"])
@jwt_required()
def update_contact(contact_id):
    try:
        data=request.get_json()
        user_id=int(get_jwt_identity())
        role=get_jwt().get("role")
        contact=ContactService.update_contact(
            contact_id,
            data,
            user_id,
            role
        )
    except ValueError:
        return jsonify({"message": "Contact not found"}), 404
    except PermissionError:
        return jsonify({"message": "Forbidden"}), 403
    return jsonify({
        "id":contact.id,
        "name":contact.name,
        "phone":contact.phone,
        "email":contact.email,
        "owner_id":contact.owner_id
    }), 200

@contact_bp.route("/contacts/<int:contact_id>",methods=["DELETE"])
@jwt_required()
def delete_contact(contact_id):
    try:
        user_id=int(get_jwt_identity())
        role=get_jwt().get("role")
        result=ContactService.delete_contact(contact_id, user_id, role)
    except ValueError:
        return jsonify({"message": "Contact not found"}), 404
    except PermissionError:
        return jsonify({"message": "Forbidden"}), 403
    return jsonify({"message": "Contact deleted"}), 200
