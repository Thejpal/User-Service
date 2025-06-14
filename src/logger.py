import logging, sys, json
from datetime import datetime

from src.settings import settings
from src.context import request_context

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.now().isoformat(),
            "level_name":record.levelname,
            "request_id": request_context.get().get("request_id"),
            "message": record.getMessage(),
            "name": record.name,
            "filename": record.filename,
            "function": record.funcName,
            "line": record.lineno
        }

        return json.dumps(log_record)

# Get logger
logger = logging.getLogger(settings.service_name)

# Create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("logs/app.log")

# Set format for the logged messages
stream_handler.setFormatter(JSONFormatter())
file_handler.setFormatter(JSONFormatter())

# Add handlers to the logger
logger.handlers = [stream_handler, file_handler]

# Set log level
logger.setLevel(logging.INFO)