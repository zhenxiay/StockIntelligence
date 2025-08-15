'''
This module sets up a logger for the application.
'''

import sys
from loguru import logger
from functools import wraps

def get_logger():
    '''
    Logger function used by other modules to log messages.
    '''
    logger.add(
        sys.stderr, 
        format="{time} {level} {message}", 
        level="INFO")

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
            result = func(*args, logger,**kwargs)
            logger.info(f"Exiting: {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}")
            raise
    return wrapper
