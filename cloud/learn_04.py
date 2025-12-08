# **************************************************
# What is this file about?
# **************************************************
import sys

sys.path.append("..")

import os
import time
from ollama import Client
from dtx_dotenv import get_key_value

from rich import print
from rich.console import Console
from rich.markdown import Markdown

TEMPERATURE: float = 0.2
BASE_URL: str = "https://ollama.com".strip().lower()
MODEL_NAME: str = "gpt-oss:20b-cloud".strip().lower()
KEY_NAME_OLLAMA_API_KEY: str = "OLLAMA_API_KEY".strip().upper()

SYSTEM_PROMPT: str = """
Role:
Expert File Content Analyst

Instruction:
You are an advanced AI system specialized in file content analysis. When the user provides the content of any file (text, code, data, markup, configuration, etc.), your task is to identify exactly what kind of file it is and provide a clear, structured explanation of its purpose, structure, and meaning.
Follow these precise rules:
Identify the file type – Determine whether the content belongs to a specific format or domain (e.g., Python script, JSON data, HTML page, Markdown document, configuration file, log file, etc.).
Explain the content – Describe what the file does, represents, or contains in a factual, technical, and concise manner.
Highlight key features – Summarize important sections, functions, variables, tags, or elements within the file.
Avoid assumptions – If you are not certain about part of the content, state your uncertainty explicitly.
Be structured and analytical – Organize your output in clear sections:

File Type:
Purpose / Function:
Structure Overview:
Key Components or Elements:
Additional Notes / Uncertainties:

You must never execute or modify the content — only analyze and describe it.
"""

# SYSTEM_PROMPT: str = """
# Role:
# Expert File Content Analyst

# Instruction:
# You are an advanced AI system specialized in file content analysis. When the user provides the content of any file (text, code, data, markup, configuration, etc.), your task is to identify exactly what kind of file it is and provide a clear, structured explanation of its purpose, structure, and meaning.

# Follow these precise rules:

# - Identify the file type – Determine whether the content belongs to a specific format or domain (e.g., Python script, JSON data, HTML page, Markdown document, configuration file, log file, etc.).
# - Explain the content – Describe what the file does, represents, or contains in a factual, technical, and concise manner.
# - Highlight key features – Summarize important sections, functions, variables, tags, or elements within the file.
# - Avoid assumptions – If you are not certain about part of the content, state your uncertainty explicitly.
# - Be structured and analytical – Organize your output in clear sections:

#     - نوع فایل:
#     - هدف / عملکرد فایل:
#     - ساختار کلی:
#     - اجزای کلیدی یا عناصر مهم:
#     - یادداشت‌ها یا موارد نامطمئن:

# - Language requirement: All explanations and descriptions must be written entirely in Persian (Farsi), using a technical, precise, and professional tone suitable for IT and software analysis contexts.

# - You must never execute, interpret, or modify the content — only analyze and describe it.
# """

SYSTEM_MESSAGE: dict = {"role": "system", "content": SYSTEM_PROMPT}


def main() -> None:
    """Main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    while True:
        print("=" * 50)
        file_path: str = input("File Path: ").strip()

        if file_path.lower() in ["bye", "exit", "quit"]:
            break

        if not os.path.exists(path=file_path):
            print(f"[-] The file '{file_path}' does not exist!\n")
            continue

        if not os.path.isfile(path=file_path):
            print(f"[-] The file '{file_path}' does not exist!\n")
            continue

        with open(file=file_path, mode="rt", encoding="utf-8") as file:
            file_content: str = file.read()

        api_key: str = get_key_value(
            key=KEY_NAME_OLLAMA_API_KEY,
        )

        headers: dict = {"Authorization": f"Bearer {api_key}"}

        client = Client(
            host=BASE_URL,
            headers=headers,
        )

        messages: list[dict] = []
        messages.append(SYSTEM_MESSAGE)

        user_prompt: str = f"File Content:\n{file_content}"
        user_message: dict = {"role": "user", "content": user_prompt}
        messages.append(user_message)

        start_time: float = time.time()

        response = client.chat(
            model=MODEL_NAME,
            messages=messages,
            options={"temperature": TEMPERATURE},
        )

        response_time: float = time.time() - start_time

        assistant_answer: str | None = response.message.content

        if assistant_answer:
            print("-" * 50)
            console = Console()
            markdown = Markdown(markup=assistant_answer)
            console.print(markdown)
            print("-" * 50)
            print(f"Response Time: {response_time:.2f} seconds.")
            print("=" * 50)
            print()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print(f"[-] {error}!")

    print()
