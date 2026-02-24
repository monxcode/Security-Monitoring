# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.logger import setup_logger

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Setup structured logging
    setup_logger(app)

    # Import and register routes
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Create tables and default admin user
    with app.app_context():
        db.create_all()
        from app.models import User
        from werkzeug.security import generate_password_hash
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                password=generate_password_hash('admin')
            )
            db.session.add(admin)
            db.session.commit()

    return app