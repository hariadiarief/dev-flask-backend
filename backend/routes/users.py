from flask import Blueprint, jsonify, request, Response

from backend.routes import basic_auth

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("", methods=["GET"])
@basic_auth.login_required
def get_all_users():
    all_users = [{"id": 1, "name": "joe"}, {"id": 2, "name": "bob"}]
    return jsonify(all_users)

@users_bp.route("", methods=["POST"])
def create_user():
    d = request.json
    print(d)
    return Response(status=204)