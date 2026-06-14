"""
Dariush Tasdighi 'logging' Package Module
"""

import logging
import dt_utility

from typing import Final
from rich.logging import RichHandler

VERSION: Final[str] = "1.6"

FILE_MODE: Final[str] = "at"
FILE_ENCODING: Final[str] = "utf-8"
DATE_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"

CONSOLE_FORMAT: Final[str] = (
    "%(asctime)s,%(msecs)3d [%(filename)s:%(lineno) 3d] - %(message)s"
)

FILE_FORMAT: Final[str] = (
    "[%(levelname)-8s] %(asctime)s,%(msecs)3d [%(filename)s:%(lineno) 3d] - %(message)s"
)


def setup_logging(
    console_level=logging.DEBUG,
    file_level=logging.WARNING,
    file_path: str = "./app.log",
) -> None:
    """
    Setup logging
    """

    root = logging.getLogger()

    # Let handlers decide what to emit
    # keep root at lowest useful level
    root.setLevel(level=logging.DEBUG)

    # از بین بردن تمام پیش‌فرض‌ها
    # Remove existing handlers for
    # avoiding duplicate logs on reconfigure!
    for handler in root.handlers:
        root.removeHandler(hdlr=handler)

    # Console Handler:

    # console_handler = logging.StreamHandler()
    console_handler = RichHandler(show_time=False)

    console_formatter = logging.Formatter(
        fmt=CONSOLE_FORMAT,
        datefmt=DATE_FORMAT,
    )

    console_handler.setLevel(level=console_level)
    console_handler.setFormatter(fmt=console_formatter)

    root.addHandler(hdlr=console_handler)

    # File Handler:

    file_handler = logging.FileHandler(
        mode=FILE_MODE,
        filename=file_path,
        encoding=FILE_ENCODING,
    )

    file_formatter = logging.Formatter(
        fmt=FILE_FORMAT,
        datefmt=DATE_FORMAT,
    )

    file_handler.setLevel(level=file_level)
    file_handler.setFormatter(fmt=file_formatter)

    root.addHandler(hdlr=file_handler)


if __name__ == "__main__":
    dt_utility.display_just_one_error_message(
        error_message=dt_utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
