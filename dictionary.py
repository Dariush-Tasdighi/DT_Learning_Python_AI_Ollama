"""
Dariush Tasdighi - AI Dictionary
"""

from typing import (
    Dict,
    List,
    Final,
)

from dt_utility import (
    clear_screen,
    format_seconds,
    display_divider,
    display_main_divider,
    display_tiny_divider,
    display_error_message,
    display_title_message,
)

from dt_lm import (
    ROLE_USER,
    ROLE_SYSTEM,
    USER_PROMPT,
    EXIT_COMMANDS,
    KEY_NAME_ROLE,
    KEY_NAME_CONTENT,
    MESSAGE_NO_CONTENT_RECEIVED,
)

from dt_ollama import chat

from rich import print
from rich.console import Console
from rich.markdown import Markdown

VERSION: Final[str] = "1.0.0"

TEMPERATURE: Final[float] = 0.0

# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()  # هیچ جوابی نمی‌دهد
# MODEL_NAME: Final[str] = "llama3.2:3b".replace(" ", "").lower()  # نسبتا دری وری جواب می‌دهد
# MODEL_NAME: Final[str] = "llama3.1:8b".replace(" ", "").lower()  # تقریبا جواب خوبی می‌دهد
# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()  # دری وری جواب می‌دهد
# MODEL_NAME: Final[str] = "gemma3:4b".replace(" ", "").lower()  # دری وری جواب می‌دهد
# MODEL_NAME: Final[str] = "gemma3:12b".replace(" ", "").lower()  # عالی انجام می‌دهد
MODEL_NAME: Final[str] = "gemma4:e2b".replace(" ", "").lower()  # خوب انجام می‌دهد
# MODEL_NAME: Final[str] = "gemma4:e4b".replace(" ", "").lower()  # خوب انجام می‌دهد

# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."

SYSTEM_PROMPT: Final[str] = """
You are a professional translator assistant from English language to Farsi language.

User must write just one word in English language.

If user wrote more than one word, or one word but \
not in English language, answer 'Error! Try Again...'.

Just translate English word, based on the below instructions:

Write the translated to Farsi language of user word in ## part.
Write the English Pronounce of user word in ### part.
Write the 5 English Synonyms in #### parts.
Write the 2 English Antonyms in ##### parts.
Write the 2 sample and simple English sentences in ###### parts.

Just write the below text, based on above instructions and \
replace '##', ''###', '####', '#####', '######' \
with your answers and never write '#' in your result at all!

Translated to Farsi Language: ##
English Pronounce: ###

Synonyms:

1) ####
2) ####
3) ####
4) ####
5) ####

Antonyms:

1) #####
2) #####

Two Sample Sentences:

1) ######
2) ######
""".strip()

SYSTEM_MESSAGE: Final[Dict] = {
    KEY_NAME_ROLE: ROLE_SYSTEM,
    KEY_NAME_CONTENT: SYSTEM_PROMPT,
}


def main() -> None:
    """Main function"""

    while True:
        clear_screen()
        display_main_divider()

        message: str = f"Dariush Tasdighi - AI Dictionary ({VERSION})"
        display_title_message(message=message)
        display_divider()

        user_prompt: str = input(USER_PROMPT).strip()

        if not user_prompt:
            continue

        if user_prompt.lower() in EXIT_COMMANDS:
            break

        messages: List[Dict] = []
        messages.append(SYSTEM_MESSAGE)

        user_message: Dict = {
            KEY_NAME_ROLE: ROLE_USER,
            KEY_NAME_CONTENT: user_prompt,
        }

        messages.append(user_message)

        assistant_answer, elapsed_time, prompt_tokens, completion_tokens = chat(
            messages=messages,
            model_name=MODEL_NAME,
            temperature=TEMPERATURE,
        )

        formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

        if not assistant_answer:
            assistant_answer = MESSAGE_NO_CONTENT_RECEIVED

        display_divider()
        console = Console()
        markdown = Markdown(markup=assistant_answer)
        console.print(markdown)

        display_divider()
        print(f"Prompt (Input) Tokens.....: {prompt_tokens}")

        display_tiny_divider()
        print(f"Completion (Output) Tokens: {completion_tokens}")

        display_divider()
        print(f"Elapsed Time..............: {formatted_elapsed_time}")

        display_main_divider()
        print()

        input("Press [ENTER] to continue... ")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()

    except Exception as error:
        display_divider()
        display_error_message(message=str(error))

    finally:
        display_main_divider()
        print()
