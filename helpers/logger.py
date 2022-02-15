import logging

def initiate_logger(logger_tittle: str):
    logger = logging.getLogger(logger_tittle)
    return logger
