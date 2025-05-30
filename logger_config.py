import logging
import os

def setup_logger(name, log_file='test.log', level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding multiple handlers if logger is reused
    if logger.hasHandlers():
        return logger

    # Clear previous logs on first run
    if os.path.exists(log_file):
        open(log_file, 'w').close()

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
