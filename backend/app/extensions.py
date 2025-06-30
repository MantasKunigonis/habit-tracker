from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Database setup and migrations
db = SQLAlchemy()
migrate = Migrate()

# User authentication management
login_manager = LoginManager()
