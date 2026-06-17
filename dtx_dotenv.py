"""
Dariush Tasdighi Custom 'dotenv' Package Module
"""

import os
import logging
import dt_utility as utility

from typing import Final
from typing import Optional
from dotenv import load_dotenv

VERSION: Final[str] = "1.5"

logger = logging.getLogger(name=__name__)
logger.addHandler(hdlr=logging.NullHandler())


def get_key_value(key: str) -> str:
    """Get key value."""

    logger.debug(msg="The '.env' file is loading...")

    load_dotenv(override=True)

    logger.debug(msg="The '.env' file loaded.")

    value: Optional[str] = os.getenv(key=key)

    if not value:
        error_message: str = f"The key '{key}' not found or is empty"
        logger.error(msg=error_message)
        raise Exception(error_message)

    logger.debug(msg=f"The key '{key}' value is valid.")

    return value


if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
