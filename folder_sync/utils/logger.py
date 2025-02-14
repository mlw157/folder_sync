import logging
from logging import getLogger


# https://www.youtube.com/watch?v=-ARI4Cz-awo&ab_channel=CoreySchafer

def init_logger(log_file):
    """configure a logger for both file and console"""
    logger = getLogger("folder_sync")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(message)s'
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)



    return logger