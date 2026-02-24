# app/logger.py
import logging
import json
from flask import has_request_context, request
from datetime import datetime

class StructuredFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'level': record.levelname,
            'action': getattr(record, 'action', 'UNKNOWN'),
            'username': getattr(record, 'username', 'anonymous'),
            'ip': getattr(record, 'ip', '0.0.0.0'),
            'message': record.getMessage()
        }
        if has_request_context():
            log_obj['ip'] = request.remote_addr
            if hasattr(request, 'user') and request.user:
                log_obj['username'] = request.user
        return json.dumps(log_obj)

def setup_logger(app):
    handler = logging.FileHandler('logs/app.log')
    handler.setFormatter(StructuredFormatter())
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    # Replace Flask's default logger
    app.logger.handlers = [handler]

def log_action(action, username=None, **kwargs):
    from flask import has_request_context, request
    from flask import current_app
    extra = {'action': action}
    if username:
        extra['username'] = username
    if has_request_context():
        extra['ip'] = request.remote_addr
        if not username and hasattr(session, 'username'):
            extra['username'] = session.get('username', 'anonymous')
    current_app.logger.info(f"Action: {action}", extra=extra)