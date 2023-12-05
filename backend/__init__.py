import os
from flask import Flask
from backend.config import Config
from dotenv import load_dotenv
from flask_migrate import Migrate

from backend.extensions import db
from backend.auth.auth import auth
from backend.routes.errors import error_bp
from backend.routes.users import users_bp
 
def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config.from_object(Config)
    
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
 
    app.register_blueprint(auth)
    app.register_blueprint(error_bp) 
    app.register_blueprint(users_bp) 
    return app