from flask import Flask
from config import Config
from dotenv import load_dotenv
from app.auth import auth_bp
from app.models import User
from app.extensions import db, migrate, login_manager
from app.api.api import api
from flask_cors import CORS

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, supports_credentials=True)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main
    app.register_blueprint(main)
    app.register_blueprint(auth_bp)

    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    api.init_app(app)

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    return {'error': 'Unauthorized access'}, 401
