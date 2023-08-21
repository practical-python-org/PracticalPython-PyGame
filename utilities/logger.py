"""
Allows us to use logging across the entire application.
"""
import logging
import pathlib


logging.basicConfig(filename=pathlib.Path('log.txt'),
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M.%S',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_debug(thing: object):
    """ Logs at the debug level """
    logger.debug(thing)


def log_info(thing: object):
    """ Logs at the info level """
    print(thing)
    logger.info(thing)


def log_warn(thing: object):
    """ Logs at the warn level """
    print(thing)
    logger.warning(thing)


def log_critical(thing: object):
    """ Logs at the critical level """
    print(thing)
    logger.critical(thing)