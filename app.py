"""
Simple Chatbot using Ollama service
"""

import os
import time
from rich import print
import dt_ollama as ollama

# from dt_ollama import chat
import dt_llm_utility as utility


def main() -> None:
    """The main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    messages: list[dict] = []
    messages.append(ollama.SYSTEM_MESSAGE)

    while True:
        print("=" * 50)
        user_prompt: str = input(utility.QUESTION_PROMPT).strip()

        if user_prompt.lower() in utility.EXIT_COMMANDS:
            break

        user_message: dict = {
            utility.KEY_NAME_ROLE: utility.ROLE_USER,
            utility.KEY_NAME_CONTENT: user_prompt,
        }
        messages.append(user_message)

        start_time: float = time.time()

        assistant_answer, prompt_tokens, completion_tokens = ollama.chat(
            # notify=True,
            messages=messages,
        )

        response_time: float = time.time() - start_time

        if not assistant_answer:
            messages.pop()
            assistant_answer = utility.MESSAGE_NO_CONTENT_RECEIVED
        else:
            assistant_message: dict = {
                utility.KEY_NAME_ROLE: utility.ROLE_ASSISTANT,
                utility.KEY_NAME_CONTENT: assistant_answer,
            }
            messages.append(assistant_message)

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
        print()

    except Exception as error:
        print(f"[-] {error}!")

    print()
