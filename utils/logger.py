"""
utils/logger.py

Application Logger
"""

import logging
import os


LOG_DIR = "logs"

os.makedirs(
    LOG_DIR,
    exist_ok=True
)

LOG_FILE = os.path.join(
    LOG_DIR,
    "application.log"
)


def get_logger(name):

    logger = logging.getLogger(name)

    logger.setLevel(
        logging.INFO
    )

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        )

        file_handler = logging.FileHandler(
            LOG_FILE
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )

    return logger
