import logging, os, sys
from datetime import datetime

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

current_date = datetime.now().strftime("%m_%d_%Y")
date_dir = os.path.join(log_dir, current_date)
os.makedirs(date_dir, exist_ok=True)

current_day = datetime.now().strftime("%A")
day_dir = os.path.join(date_dir, current_day)
os.makedirs(day_dir, exist_ok=True)

def create_directory_with_timestamp(base_time):
    timestamp = base_time.strftime("%m_%d_%Y_%H_%M")
    timestamp_dir = os.path.join(day_dir, timestamp)
    os.makedirs(timestamp_dir, exist_ok=True)
    return timestamp_dir

base_time = datetime.now()
timestamp_dir = create_directory_with_timestamp(base_time)

info_log_filepath = os.path.join(timestamp_dir, "info.log")
error_log_filepath = os.path.join(timestamp_dir, "error.log")

logs_format = "[ [%(asctime)s] : %(levelname)s : %(name)s : %(module)s : %(lineno)d : %(message)s ]"

logger = logging.getLogger('usa_visa')
logger.setLevel(logging.INFO)

if not logger.handlers:
    # INFO level handler
    info_handler = logging.FileHandler(info_log_filepath)
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(logging.Formatter(logs_format))

    # ERROR level handler
    error_handler = logging.FileHandler(error_log_filepath)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter(logs_format))

    # console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(logs_format))

    # add handler to logger
    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

