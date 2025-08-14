'''
This module sets up a logger for the application.
'''

import logging
from functools import wraps

def get_logger():
    '''
    Logger function used by other modules to log messages.
    '''
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # Add a StreamHandler to output logs to the console
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

def log_function(func):
    '''
    Decorator to log function entry, exit, and exceptions.
    '''
    # create logger and pass it to the wrapper function
    logger = get_logger()
    # define the wrapper function with the same signature as the original function
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Logger initialized: {func.__name__}")
        try:
            result = func(logger, *args, **kwargs)
            logger.info(f"Exiting: {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}")
            raise
    return wrapper