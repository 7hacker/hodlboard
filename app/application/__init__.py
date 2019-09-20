from flask import Flask, g

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)

    if app.config["ENV"] == "production":
        app.config.from_object("config.Production")
    elif app.config["ENV"] == "staging":
        app.config.from_object("config.Staging")
    elif app.config["ENV"] == "development":
        app.config.from_object("config.Local")
    else:
        app.config.from_object("config.Config")
    #app.config.from_object('config.Config')

    with app.app_context():
        # Include our Routes
        from . import routes
        return app
