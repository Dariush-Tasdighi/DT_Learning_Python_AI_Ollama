"""
Dariush Tasdighi - Utility Module
"""

import os
import sys
import subprocess

from typing import (
    Final,
    Optional,
)

from rich import print
from datetime import datetime

# Major, Minor, Patch (Revision)
# VERSION: Final[str] = "0.1.0"
VERSION: Final[str] = "2.0.3"


def clear_screen() -> None:
    """Clear screen"""

    subprocess.run(
        shell=True,
        check=True,
        capture_output=False,
        args="cls" if os.name == "nt" else "clear",
    )


def display_divider(character: str = "-", count: int = 50, color: str = "cyan") -> None:
    """Display divider"""

    print(f"[{color}]{character * count}[/{color}]")


def display_main_divider(character: str = "=", count: int = 50, color: str = "cyan bold") -> None:
    """Display main divider"""

    display_divider(character=character, count=count, color=color)


def display_tiny_divider(character: str = ".", count: int = 50, color: str = "bright_black") -> None:
    """Display tiny divider"""

    display_divider(character=character, count=count, color=color)


def fix_text(text: Optional[str]) -> str:
    """Fix text"""

    if text is None:
        return ""

    text = text.strip()
    if text == "":
        return ""

    while "  " in text:
        text = text.replace("  ", " ")

    return text


def get_word_count(text: str) -> int:
    """Get word count"""

    result: int = len(text.split(sep=" "))
    return result


def display_title_message(message: str) -> None:
    """Display title message"""

    message = fix_text(text=message)
    if message == "":
        return

    message = message.title()
    result: str = f"[cyan bold]{message}[/cyan bold]"
    print(result)


def display_error_message(message: str) -> None:
    """Display error message"""

    message = fix_text(text=message)
    if message == "":
        return

    if not message.endswith("!"):
        message += "!"

    result: str = f"[red bold]🔴 {message}[/red bold]"
    print(result)


def display_success_message(message: str) -> None:
    """Display success message"""

    message = fix_text(text=message)
    if message == "":
        return

    if not message.endswith("."):
        message += "."

    result: str = f"[green bold]✅ {message}[/green bold]"
    print(result)


def display_warning_message(message: str) -> None:
    """Display warning message"""

    message = fix_text(text=message)
    if message == "":
        return

    if not message.endswith("!"):
        message += "!"

    result: str = f"[yellow bold]⚠️  {message}[/yellow bold]"
    print(result)


def display_information_message(message: str) -> None:
    """Display information message"""

    message = fix_text(text=message)
    if message == "":
        return

    if not message.endswith("."):
        message += "."

    result: str = f"[blue]ℹ️  {message}[/blue]"
    print(result)


def display_just_one_error_message(message: str) -> None:
    """Display just one error message"""

    clear_screen()

    message = fix_text(text=message)
    if message == "":
        return

    message_length: int = len(message) + 4

    display_main_divider(count=message_length)
    display_error_message(message=message)
    display_main_divider(count=message_length)
    print()

    sys.exit(1)


def prevent_direct_execution() -> None:
    """Prevent direct execution"""

    message: str = "This module is designed to be imported, not executed directly"

    display_just_one_error_message(message=message)


def get_formated_now(with_miliseconds: bool = False) -> str:
    """Get formated now"""

    now = datetime.now()

    formated_now: str

    if not with_miliseconds:
        formated_now = now.strftime(format="%Y_%m_%d_%H_%M_%S")
    else:
        formated_now = now.strftime(format="%Y_%m_%d_%H_%M_%S_%f")[:-3]

    return formated_now


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


def check_file_exists(file_path: str) -> bool:
    """Check file exists"""

    if not os.path.exists(path=file_path):
        return False

    if not os.path.isfile(path=file_path):
        return False

    return True


def check_file_exists_force(file_path: str) -> None:
    """Check file exists (Force)"""

    result: bool = check_file_exists(file_path=file_path)
    if not result:
        message: str = f"The file '{file_path}' does not exist"
        display_just_one_error_message(message=message)


def check_path_exists(path: str) -> bool:
    """Check path exists"""

    if not os.path.exists(path=path):
        return False

    if os.path.isfile(path=path):
        return False

    return True


def check_path_exists_force(path: str) -> None:
    """Check path exists (Force)"""

    message: str = f"The path '{path}' does not exist"

    result: bool = check_path_exists(path=path)
    if not result:
        display_just_one_error_message(message=message)


if __name__ == "__main__":
    prevent_direct_execution()
