# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import User
from app.auth import login_required, login_user, logout_user
from app.logger import log_action

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user)
            log_action('LOGIN_SUCCESS', username=username)
            return redirect(url_for('main.dashboard'))
        else:
            log_action('LOGIN_FAILURE', username=username)
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@main.route('/dashboard')
@login_required
def dashboard():
    username = session.get('username')
    log_action('PAGE_VISIT', username=username, action='dashboard')
    return render_template('dashboard.html', username=username)

@main.route('/logout')
def logout():
    username = session.get('username', 'anonymous')
    logout_user()
    log_action('LOGOUT', username=username)
    return redirect(url_for('main.login'))