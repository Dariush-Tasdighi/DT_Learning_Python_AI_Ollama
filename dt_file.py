"""
Dariush Tasdighi File Utility Module
"""

import os
import json
import dt_utility as utility

from typing import (
    Any,
    Final,
    Optional,
)

VERSION: Final[str] = "1.0.2"


def save_text_file(text: str, file_path: str) -> None:
    """
    Save text file
    """

    with open(file=file_path, mode="wt", encoding="utf-8") as file:
        file.write(text)


def load_text_file(file_path: str) -> Optional[str]:
    """
    Load text file
    """

    if not os.path.exists(path=file_path):
        return None

    if not os.path.isfile(path=file_path):
        return None

    with open(file=file_path, mode="rt", encoding="utf-8") as file:
        text: str = file.read()
        return text


def serialize(obj) -> str:
    """
    Serialize object
    """

    json_string: str = json.dumps(
        obj,
        indent=4,
        default=lambda o: o.__dict__,
    )

    return json_string


def serialize_and_save(obj, file_path: str) -> None:
    """
    Serialize object and save it to file
    """

    json_string: str = serialize(obj=obj)

    save_text_file(
        text=json_string,
        file_path=file_path,
    )


def deserialize(json_string: str) -> Any:
    """
    Deserialize string
    """

    result = json.loads(s=json_string)
    return result


def load_and_deserialize(file_path: str) -> Any:
    """
    Load file and deserialize
    """

    text: Optional[str] = load_text_file(file_path=file_path)

    if text == None:
        return None

    result = deserialize(json_string=text)
    return result


if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
