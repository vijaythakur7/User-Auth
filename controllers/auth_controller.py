from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services import auth_service
from config import Config

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    payload, status = auth_service.register(request.get_json())
    return jsonify(payload), status


@auth_bp.route("/login", methods=["POST"])
def login():
    payload, status = auth_service.login(request.get_json())
    return jsonify(payload), status


@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    
    service_key = request.headers.get("X-Service-Key")

    if service_key != Config.INVENTORY_SERVICE_KEY:
        return jsonify({
        "message": "Unauthorized service"
    }), 401

    payload, status = auth_service.profile(get_jwt_identity())
    return jsonify(payload), status
