from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required
from .models import User, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            current_app.logger.info(f"User login successful", extra={'action': 'LOGIN_SUCCESS'})
            return redirect(url_for('routes.dashboard'))
        
        current_app.logger.warning(f"Failed login attempt for {username}", extra={'action': 'LOGIN_FAILURE'})
        flash('Invalid username or password')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    current_app.logger.info(f"User logged out", extra={'action': 'LOGOUT'})
    logout_user()
    return redirect(url_for('auth.login'))