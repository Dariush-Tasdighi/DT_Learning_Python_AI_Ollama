"""
Dariush Tasdighi LLM Utility Module
"""

from typing import Final
import dt_utility as utility

VERSION: Final[str] = "2.3"

USER_QUESTION: Final[str] = "User: "

EXIT_COMMANDS: Final[list[str]] = [
    "bye".replace(" ", "").lower(),
    "exit".replace(" ", "").lower(),
    "quit".replace(" ", "").lower(),
]

MESSAGE_GOODBYE: Final[str] = "Goodbye"
MESSAGE_NO_CONTENT_RECEIVED: Final[str] = "No content received!"

ROLE_USER: Final[str] = "user".replace(" ", "").lower()
ROLE_SYSTEM: Final[str] = "system".replace(" ", "").lower()
ROLE_ASSISTANT: Final[str] = "assistant".replace(" ", "").lower()

KEY_NAME_ROLE: Final[str] = "role".replace(" ", "").lower()
KEY_NAME_CONTENT: Final[str] = "content".replace(" ", "").lower()
KEY_NAME_TEMPRETURE: Final[str] = "temperature".replace(" ", "").lower()

SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."

SYSTEM_MESSAGE: Final[dict] = {
    KEY_NAME_ROLE: ROLE_SYSTEM,
    KEY_NAME_CONTENT: SYSTEM_PROMPT,
}

if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
