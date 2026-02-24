import os
from flask import Flask
from .models import db, create_default_admin
from .routes import main
from .logger import setup_logger

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "supersecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    setup_logger()

    with app.app_context():
        db.create_all()
        create_default_admin()

    app.register_blueprint(main)

    return app