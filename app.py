# **************************************************
"""
Simple Chatbot using Ollama service
"""

import time
import dt_llm_utility as llm_utility

# NEW
# import dt_ollama as ollama
import dtx_ollama as ollama

from dt_utility import (
    clear_screen,
    format_seconds,
    display_error_message,
    display_warning_message,
)

from rich import print
from rich.console import Console
from rich.markdown import Markdown


def main() -> None:
    """The main of program"""

    clear_screen()

    messages: list[dict] = []
    messages.append(llm_utility.SYSTEM_MESSAGE)

    while True:
        print("=" * 50)
        user_prompt: str = input(llm_utility.USER_QUESTION).strip()

        if user_prompt.lower() in llm_utility.EXIT_COMMANDS:
            display_warning_message(message=llm_utility.MESSAGE_GOODBYE)
            print("=" * 50)
            break

        user_message: dict = {
            llm_utility.KEY_NAME_ROLE: llm_utility.ROLE_USER,
            llm_utility.KEY_NAME_CONTENT: user_prompt,
        }

        messages.append(user_message)

        start_time: float = time.perf_counter()

        # assistant_answer, prompt_tokens, completion_tokens = ollama.chat(
        #     # NEW
        #     # notify=True,
        #     messages=messages,
        # )

        assistant_answer, prompt_tokens, completion_tokens = ollama.chat(
            messages=messages,
            # NEW
            model_name="gpt-oss:20b-cloud",
        )

        end_time: float = time.perf_counter()
        elapsed_time: float = end_time - start_time
        formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

        if not assistant_answer:
            messages.pop()
            assistant_answer = llm_utility.MESSAGE_NO_CONTENT_RECEIVED
        else:
            assistant_message: dict = {
                llm_utility.KEY_NAME_ROLE: llm_utility.ROLE_ASSISTANT,
                llm_utility.KEY_NAME_CONTENT: assistant_answer,
            }

            messages.append(assistant_message)

        print("-" * 50)
        console = Console()
        markdown = Markdown(markup=assistant_answer)
        console.print(markdown)
        print("-" * 50)
        print(f"Elapsed Time: {formatted_elapsed_time}")
        print("-" * 50)
        print(f"Prompt Tokens (Input): {prompt_tokens}")
        print("-" * 50)
        print(f"Completion Tokens (Output): {completion_tokens}")
        print("=" * 50)
        print()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()
        print("=" * 50)

    except Exception as exception:
        print()
        display_error_message(message=str(exception))
        print("=" * 50)

    finally:
        print()
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# > curl https://api.ipify.org
# > curl -4 https://api.ipify.org
# > curl -6 https://api.ipify.org
# > Invoke-WebRequest https://api.ipify.org
# > curl https://api.ipify.org --socks5 127.0.0.1:10808
# > curl https://api.ipify.org --proxy socks5://127.0.0.1:10808
#
# > netsh winhttp show proxy
# [OUTPUT] Direct access (no proxy server)
#
# [SET JUST IN CURRENT POWERSHELL SESSION]
# > $env:HTTP_PROXY="socks5://127.0.0.1:10808"
# > $env:HTTPS_PROXY="socks5://127.0.0.1:10808"
#
# [DISPLAY]
# > $env:HTTP_PROXY
# > $env:HTTPS_PROXY
#
# [REMOVE]
# $env:HTTP_PROXY = $null
# $env:HTTPS_PROXY = $null
#
# > curl https://api.ipify.org
#
# > pip install httpx[socks]
# **************************************************
# **************************************************
# **************************************************
