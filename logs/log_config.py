import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

def setup_logger():
    # Define the main directory for logs
    main_log_directory = "logs"
    # Define the subdirectory for daily logs
    daily_log_directory = os.path.join(main_log_directory, "daily_logs")
    
    # Check and create directories if they don't exist
    if not os.path.exists(main_log_directory):
        os.makedirs(main_log_directory)
    if not os.path.exists(daily_log_directory):
        os.makedirs(daily_log_directory)

    # Get today's date to use in the filename
    today_date = datetime.now().strftime("%Y-%m-%d")
    log_filename = os.path.join(daily_log_directory, f"{today_date}.log")
    
    # Setup the logger
    logger = logging.getLogger("SpamMLLogger")
    logger.setLevel(logging.INFO)
    
    # Check if handlers are already set up to avoid duplication
    if not logger.handlers:
        handler = TimedRotatingFileHandler(log_filename, when="midnight", interval=1, backupCount=7)
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    # Prevent logging from propagating to the root logger
    logger.propagate = False
    
    return logger

# Initialize and export the logger
logger = setup_logger()
