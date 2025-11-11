"""
Dariush Tasdighi 'dotenv' utility module.
"""

import os
import logging
from dotenv import load_dotenv

VERSION: str = "1.1"

logger = logging.getLogger(name=__name__)
logger.addHandler(hdlr=logging.NullHandler())


def get_key_value(key: str) -> str:
    """Get key value function."""

    logger.debug(msg="'.env' file is loading...")

    load_dotenv(override=True)

    logger.debug(msg="'.env' file loaded.")

    value: str | None = os.getenv(key=key)

    if not value:
        logger.error(msg=f"Key '{key}' not found or is empty!")
        exit()

    logger.debug(msg=f"The key '{key}' value is valid.")

    return value


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!\n")
