# **************************************************
"""
Dictionary Assistant (Offline).
This is a simple dictionary assistant that translates English words to Farsi language.
"""

import os
import time
from rich import print
import dt_ollama as ollama
import dt_llm_utility as utility
from rich.console import Console
from rich.markdown import Markdown

TEMPERATURE: float = 0

# MODEL_NAME: str = "llama3.2:1b".strip().lower()  # هیچ جوابی نمی‌دهد
# MODEL_NAME: str = "llama3.2:3b".strip().lower()  # نسبتا دری وری جواب می‌دهد
MODEL_NAME: str = "llama3.1:8b".strip().lower()  # تقریبا جواب خوبی می‌دهد
# MODEL_NAME: str = "gemma3:1b".strip().lower()  # دری وری جواب می‌دهد
# MODEL_NAME: str = "gemma3:4b".strip().lower()  # دری وری جواب می‌دهد
# MODEL_NAME: str = "gemma3:12b".strip().lower()  # عالی انجام می‌دهد

# SYSTEM_PROMPT: str = "You are a helpful AI assistant."

SYSTEM_PROMPT: str = """
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
"""

SYSTEM_PROMPT = SYSTEM_PROMPT.strip()
SYSTEM_MESSAGE: dict = {
    utility.KEY_NAME_ROLE: utility.ROLE_SYSTEM,
    utility.KEY_NAME_CONTENT: SYSTEM_PROMPT,
}


def main() -> None:
    """The main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    while True:
        print("=" * 50)
        user_prompt: str = input(utility.QUESTION_PROMPT)

        if user_prompt.lower() in utility.EXIT_COMMANDS:
            break

        os.system(command="cls" if os.name == "nt" else "clear")

        messages: list[dict] = []
        messages.append(SYSTEM_MESSAGE)

        user_message: dict = {
            utility.KEY_NAME_ROLE: utility.ROLE_USER,
            utility.KEY_NAME_CONTENT: user_prompt,
        }

        messages.append(user_message)

        start_time: float = time.time()

        assistant_answer, prompt_tokens, completion_tokens = ollama.chat(
            messages=messages,
            model_name=MODEL_NAME,
            temperature=TEMPERATURE,
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
# **************************************************


# **************************************************
# """
# Dictionary Assistant (Offline).
# This is a simple dictionary assistant that translates English words to Farsi language.
# """

# import os
# import time
# from rich import print
# import dt_ollama as ollama
# import dt_llm_utility as utility
# import dictionary_constants as constants


# def main() -> None:
#     """
#     Main function.
#     """

#     os.system(command="cls" if os.name == "nt" else "clear")

#     while True:
#         print("=" * 50)
#         user_prompt: str = input(utility.QUESTION_PROMPT)

#         if user_prompt.lower() in utility.EXIT_COMMANDS:
#             break

#         os.system(command="cls" if os.name == "nt" else "clear")

#         messages: list[dict] = []
#         messages.append(constants.SYSTEM_MESSAGE)

#         user_message: dict = {
#             utility.KEY_NAME_ROLE: utility.ROLE_USER,
#             utility.KEY_NAME_CONTENT: user_prompt,
#         }

#         messages.append(user_message)

#         start_time: float = time.time()

#         assistant_answer, prompt_tokens, completion_tokens = ollama.chat(
#             messages=messages,
#             model_name=constants.MODEL_NAME,
#             temperature=constants.TEMPERATURE,
#         )

#         response_time: float = time.time() - start_time

#         if not assistant_answer:
#             assistant_answer = utility.MESSAGE_NO_CONTENT_RECEIVED

#         print("-" * 50)
#         print(assistant_answer)
#         print("-" * 50)
#         print("Prompt Tokens (Input):", prompt_tokens)
#         print("-" * 50)
#         print("Completion Tokens (Output):", completion_tokens)
#         print("-" * 50)
#         print(f"Full response received {response_time:.2f} seconds after request.")
#         print("=" * 50)
#         print()


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         pass

#     except Exception as error:
#         print(f"[-] {error}")
# **************************************************
