# README.md
# Security Monitoring Web Application

Flask-based web application with authentication, structured logging, and SQLite.

## Features
- User authentication (default admin: admin/admin)
- Dashboard accessible only after login
- Structured JSON logs for login attempts, page visits, API requests
- Logs stored in `logs/app.log`

## Setup
1. Create virtual environment: `python -m venv venv`
2. Activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python run.py`
5. Access at http://localhost:5000

## Logging Format
Each log entry is a JSON object with:
- timestamp (ISO 8601 UTC)
- level
- action (e.g., LOGIN_SUCCESS, PAGE_VISIT)
- username
- ip
- message