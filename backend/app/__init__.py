from flask import Flask
from config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .auth import auth
from app.models import User

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main
    app.register_blueprint(main)
    app.register_blueprint(auth)

    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
