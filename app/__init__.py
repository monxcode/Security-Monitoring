from flask import Flask
from .config import Config
from .models import db, User
from .logger import setup_logger
from flask_login import LoginManager

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)

    db.init_app(app)
    setup_logger(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth_bp
    from .routes import routes_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(routes_bp)

    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()

    return app