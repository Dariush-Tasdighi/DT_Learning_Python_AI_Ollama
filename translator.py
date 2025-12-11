"""
Translator Assistant (Offline).
This is a simple translator assistant that translates English paragraphs to Farsi language.
"""

import os
import time
from rich import print
import dt_ollama as ollama
import dt_llm_utility as utility
from rich.console import Console
from rich.markdown import Markdown
import translator_constants as constants


def main() -> None:
    """Main of program."""

    os.system(command="cls" if os.name == "nt" else "clear")

    while True:
        print("=" * 50)
        user_prompt: str = input(utility.QUESTION_PROMPT).strip()

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
        console = Console()
        markdown = Markdown(markup=assistant_answer)
        console.print(markdown)
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
        print()

    except Exception as error:
        print(f"[-] {error}!")

    print()
