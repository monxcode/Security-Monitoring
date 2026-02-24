# app/auth.py
from functools import wraps
from flask import session, redirect, url_for, request
from app.logger import log_action

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            log_action('UNAUTHORIZED_ACCESS', username='anonymous')
            return redirect(url_for('main.login'))
        return f(*args, **kwargs)
    return decorated_function

def login_user(user):
    session['user_id'] = user.id
    session['username'] = user.username

def logout_user():
    session.clear()