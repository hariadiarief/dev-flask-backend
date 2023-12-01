from flask import Blueprint, jsonify, request
import jwt
from werkzeug.security import check_password_hash

from backend.routes import allowed_users, secret_token


auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    d = request.json
    if "username" not in d or "password" not in d:
        raise Exception("Unable to authenticate")
    
    if not check_password_hash(allowed_users[d["username"]], d["password"]):
        raise Exception("invalid password")
    
    encode_jwt = jwt.encode({"sub":1, "name": "sergio"}, secret_token, algorithm="HS256")
    return jsonify({"token":encode_jwt})