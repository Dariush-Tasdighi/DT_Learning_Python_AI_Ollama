"""
Dariush Tasdighi 'dotenv' Package Module
"""

import os
import dt_utility

from typing import Final
from typing import Optional
from dotenv import load_dotenv

VERSION: Final[str] = "1.3"


def get_key_value(key: str) -> str:
    """
    Get key value.
    """

    load_dotenv(override=True)

    value: Optional[str] = os.getenv(key=key)

    if not value:
        error_message: str = f"The key '{key}' not found or is empty"
        raise Exception(error_message)

    return value


if __name__ == "__main__":
    dt_utility.display_just_one_error_message(
        error_message=dt_utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
