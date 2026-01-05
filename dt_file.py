"""
Dariush Tasdighi file utility module.
"""

import os
import json
from typing import Any

__version__ = "1.0"


def save_text_file(text: str, file_path: str) -> None:
    """Save text file"""

    with open(file=file_path, mode="wt", encoding="utf-8") as file:
        file.write(text)


def load_text_file(file_path: str) -> str | None:
    """Load text file"""

    if not os.path.exists(path=file_path):
        return None

    if not os.path.isfile(path=file_path):
        return None

    with open(file=file_path, mode="rt", encoding="utf-8") as file:
        text: str = file.read()
        return text


def serialize(obj) -> str:
    """Serialize"""

    json_string: str = json.dumps(
        obj,
        indent=4,
        default=lambda o: o.__dict__,
    )

    return json_string


def serialize_and_save(obj, file_path: str) -> None:
    """Serialize and save"""

    json_string: str = serialize(obj=obj)

    save_text_file(
        text=json_string,
        file_path=file_path,
    )


def deserialize(json_string: str) -> Any:
    """Deserialize"""

    result = json.loads(s=json_string)
    return result


def load_and_deserialize(file_path: str) -> Any:
    """Load and deserialize"""

    text: str | None = load_text_file(file_path=file_path)

    if text == None:
        return None

    result = deserialize(json_string=text)
    return result


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!\n")
