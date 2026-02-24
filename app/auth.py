from werkzeug.security import check_password_hash, generate_password_hash
from .models import User, db

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

def create_user(username, password):
    user = User(
        username=username,
        password=generate_password_hash(password)
    )
    db.session.add(user)
    db.session.commit()