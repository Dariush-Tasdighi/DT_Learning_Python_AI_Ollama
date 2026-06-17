"""
Dariush Tasdighi Utility Module
"""

import os
import subprocess

from rich import print
from typing import Final
from typing import Optional

VERSION: Final[str] = "1.4"
ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY: Final[str] = (
    "This module is designed to be imported, not executed directly"
)


def clear_screen() -> None:
    """
    Clear screen
    """

    subprocess.run(
        check=True,
        shell=True,
        args="cls" if os.name == "nt" else "clear",
    )


def fix_text(text: Optional[str]) -> str:
    """
    Fix text
    """

    if text == None:
        return ""

    text = text.strip()
    if text == "":
        return ""

    while "  " in text:
        text = text.replace("  ", " ")

    return text


def display_error_message(message: str) -> None:
    """
    Display an error message
    """

    message = fix_text(text=message)
    if not message.endswith("!"):
        message += "!"

    result: str = f"[red bold][-] {message}[/red bold]"
    print(result)


def display_success_message(message: str) -> None:
    """
    Display a success message
    """

    message = fix_text(text=message)
    if not message.endswith("."):
        message += "."

    result: str = f"[green bold][+] {message}[/green bold]"
    print(result)


def display_warning_message(message: str) -> None:
    """
    Display an warning message
    """

    message = fix_text(text=message)
    if not message.endswith("!"):
        message += "!"

    result: str = f"[yellow bold][!] {message}[/yellow bold]"
    print(result)


def display_information_message(message: str) -> None:
    """
    Display an information message
    """

    message = fix_text(text=message)
    if not message.endswith("."):
        message += "."

    result: str = f"[grey35][.] {message}[/grey35]"
    print(result)


def display_just_one_error_message(message: str) -> None:
    """
    Display just one error message
    """

    clear_screen()

    message = fix_text(text=message)
    if not message.endswith("!"):
        message += "!"

    message = f"[-] {message}"
    message_length: int = len(message)

    print("=" * message_length)
    print(f"[red bold]{message}[/red bold]")
    print("=" * message_length)
    print()


def format_seconds(seconds: float, display_milliseconds: bool = True) -> str:
    """
    Convert seconds into a human-readable format (H:M:S).
    If display_milliseconds is True, shows milliseconds as three decimal places in the seconds part.
    """

    if not display_milliseconds:
        # رفتار اصلی: حذف اعشار (همانند int)
        total_seconds = int(seconds)

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        remaining_seconds = total_seconds % 60

        if hours > 0:
            return f"{hours} h - {minutes} m - {remaining_seconds} s"
        elif minutes > 0:
            return f"{minutes} m - {remaining_seconds} s"
        else:
            return f"{remaining_seconds} s"
    else:
        # تبدیل کل ثانیه به میلی‌ثانیه (با رُند کردن برای دقت بیشتر)
        total_ms = int(round(seconds * 1000))

        hours = total_ms // (3600 * 1000)
        remainder = total_ms % (3600 * 1000)

        minutes = remainder // (60 * 1000)
        remainder %= 60 * 1000

        secs = remainder // 1000
        ms = remainder % 1000

        # ساخت بخش ثانیه همراه با میلی‌ثانیه (سه رقم ثابت)
        seconds_part = f"{secs}.{ms:03d} s"

        if hours > 0:
            return f"{hours} h - {minutes} m - {seconds_part}"
        elif minutes > 0:
            return f"{minutes} m - {seconds_part}"
        else:
            return seconds_part


if __name__ == "__main__":
    display_just_one_error_message(
        message=ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
