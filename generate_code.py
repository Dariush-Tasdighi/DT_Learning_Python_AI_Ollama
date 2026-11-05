"""
Generate Code Assistant (Offline).
This is a code generator for EF Core.
"""

import os
import time
from rich import print
import dt_ollama as ollama
import dt_lm as utility
import generate_code_constants as constants


def main() -> None:
    """
    Main function.
    """

    os.system(command="cls" if os.name == "nt" else "clear")

    while True:
        print("=" * 50)
        user_prompt: str = input(utility.USER_QUESTION)
        user_prompt: str = """
یک مدل می‌خواهم به نام کاربر با ویژگی‌های ذیل
نام
نام خانوادگی
شناسه کاربری - الزامی
نشانی پست الکترونیکی - الزامی
شماره تلفن همراه - الزامی
آیا نشانی پست الکترونیکی تایید شده؟
آیا شماره تلفن همراه تایید شده؟
گذروازه - الزامی
        """

        if user_prompt.lower() in utility.EXIT_COMMANDS:
            break

        os.system(command="cls" if os.name == "nt" else "clear")

        messages: list[dict] = []
        messages.append(constants.SYSTEM_MESSAGE)

        user_message: dict = {
            utility.KEY_NAME_ROLE: utility.ROLE_USER,
            utility.KEY_NAME_CONTENT: user_prompt,
        }
        messages.append(user_message)

        start_time: float = time.time()

        assistant_answer, prompt_tokens, completion_tokens = ollama.chat(
            messages=messages,
            model_name=constants.MODEL_NAME,
            temperature=constants.TEMPERATURE,
        )

        response_time: float = time.time() - start_time

        if not assistant_answer:
            assistant_answer = utility.MESSAGE_NO_CONTENT_RECEIVED

        print("-" * 50)
        print(assistant_answer)
        print("-" * 50)
        print("Prompt Tokens (Input):", prompt_tokens)
        print("-" * 50)
        print("Completion Tokens (Output):", completion_tokens)
        print("-" * 50)
        print(f"Full response received {response_time:.2f} seconds after request.")
        print("=" * 50)
        print()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print(f"[-] {error}")
