"""
Dariush Tasdighi - Language Model Utility Module
"""

from typing import (
    Dict,
    List,
    Final,
)

from dt_utility import prevent_direct_execution

VERSION: Final[str] = "3.0.0"

USER_PROMPT: Final[str] = "User: "
USER_ID_PROMPT: Final[str] = "User ID: "

EXIT_COMMANDS: Final[List[str]] = [
    "bye".replace(" ", "").lower(),
    "exit".replace(" ", "").lower(),
    "quit".replace(" ", "").lower(),
]

ROLE_USER: Final[str] = "user".replace(" ", "").lower()
ROLE_SYSTEM: Final[str] = "system".replace(" ", "").lower()
ROLE_ASSISTANT: Final[str] = "assistant".replace(" ", "").lower()

KEY_NAME_ROLE: Final[str] = "role".replace(" ", "").lower()
KEY_NAME_CONTENT: Final[str] = "content".replace(" ", "").lower()
KEY_NAME_TEMPRETURE: Final[str] = "temperature".replace(" ", "").lower()

MESSAGE_GOODBYE: Final[str] = "Goodbye"
MESSAGE_NO_CONTENT_RECEIVED: Final[str] = "No content received!"

SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."
SYSTEM_MESSAGE: Final[Dict] = {
    KEY_NAME_ROLE: ROLE_SYSTEM,
    KEY_NAME_CONTENT: SYSTEM_PROMPT,
}

if __name__ == "__main__":
    prevent_direct_execution()
