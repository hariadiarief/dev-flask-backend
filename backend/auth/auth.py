# app/auth/auth.py
from functools import wraps
from math import log
from flask import Blueprint, request, jsonify
import jwt
from flask import current_app
from backend.models.user import User

auth = Blueprint('auth', __name__)

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'] 
            
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            data = jwt.decode(token, 'key-of-success-adalah-kunci-sukses',algorithms=["HS256"])

            current_user = User.query\
                .filter_by(public_id = data['public_id'])\
                .first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated