from flask import Flask

from config import Config
from app.extensions import login_manager
from app.routes.users import users_bp
from app.routes.auth import auth_bp
from app.routes.files import files_bp
from app.util import Base32Converter
from pymongo import MongoClient


def create_app(config_class=Config):
    """
    Create a Flask application using the app factory pattern.

    Args:
        config_class (Config): The configuration settings to use

    Returns:
        app (Flask): A Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Add custom URL converters here
    app.url_map.converters["b32"] = Base32Converter

    # Create a new instance of the MongoClient class. This object will be used to interact with the MongoDB database.
    client = MongoClient(app.config["MONGO_URI"])
    app.db = client[app.config["DATABASE_NAME"]]

    # Initialize Flask extensions here
    login_manager.init_app(app)

    # Register blueprints here
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(files_bp)

    return app
