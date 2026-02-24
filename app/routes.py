from flask import Blueprint, render_template, current_app, request
from flask_login import login_required, current_user

routes_bp = Blueprint('routes', __name__)

@routes_bp.before_request
def log_request_info():
    if request.endpoint and 'static' not in request.endpoint:
        current_app.logger.info(f"Page visit: {request.path}", extra={'action': 'PAGE_VISIT'})

@routes_bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@routes_bp.route('/api/status')
@login_required
def api_status():
    current_app.logger.info("API status requested", extra={'action': 'API_REQUEST'})
    return {"status": "operational", "monitoring": True}