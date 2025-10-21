from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Config
    app.config["SECRET_KEY"] = "supersecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///agricare.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    from .routes import main
    from .api import api
    from .notify import notify

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(notify, url_prefix="/notify")

    return app
