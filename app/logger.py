import logging
import json
import os
from datetime import datetime
from pythonjsonlogger import jsonlogger
from flask import request, session

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['timestamp'] = datetime.utcnow().isoformat()
        log_record['ip_address'] = request.remote_addr if request else 'N/A'
        log_record['username'] = session.get('_user_id', 'anonymous')
        if not log_record.get('action'):
            log_record['action'] = record.getMessage()

def setup_logger(app):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    handler = logging.FileHandler(app.config['LOG_FILE_PATH'])
    formatter = CustomJsonFormatter('%(timestamp)s %(ip_address)s %(username)s %(action)s')
    handler.setFormatter(formatter)
    
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)