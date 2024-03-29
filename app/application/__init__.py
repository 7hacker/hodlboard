from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

db = SQLAlchemy()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    db.init_app(app)

    if app.config["ENV"] == "production":
        app.config.from_object("config.Production")
    elif app.config["ENV"] == "staging":
        app.config.from_object("config.Staging")
    elif app.config["ENV"] == "development":
        app.config.from_object("config.Local")
    else:
        app.config.from_object("config.Config")

    with app.app_context():
        # Include our Routes, also instruct flake8 to ignore
        from . import routes  # noqa: F401 isort:skip
        # Create tables for our models
        db.create_all()
        return app
