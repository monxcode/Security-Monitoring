import logging
import os

def setup_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s | %(message)s"
    )

def log_event(ip, username, action):
    logging.info(f"IP:{ip} | User:{username} | Action:{action}")