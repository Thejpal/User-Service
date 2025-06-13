import logging, sys, json

from src.settings import settings

# Get logger
logger = logging.getLogger(settings.service_name)

# Set the format for the log record
log_record = {
    "timestamp": "%(asctime)s",
    "level_name": "%(levelname)s",
    "message": "%(message)s",
    "name": "%(name)s",
    "filename": "%(filename)s",
    "function": "%(funcName)s",
    "line": "%(lineno)d"
}

# Create format for the log message
formatter = logging.Formatter(
    fmt = json.dumps(log_record)
)

# Create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("logs/app.log")

# Set format for the logged messages
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.handlers = [stream_handler, file_handler]

# Set log level
logger.setLevel(logging.INFO)