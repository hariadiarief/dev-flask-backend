from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

allowed_users = {
    "sergio" : generate_password_hash( "my-pass"),
    "bob" : generate_password_hash( "his-pass"),
}

basic_auth = HTTPBasicAuth() 

@basic_auth.verify_password
def verify_basic_password(username, password):
    if username not in allowed_users:
        return None
    if check_password_hash(allowed_users[username], password):
        return username
 