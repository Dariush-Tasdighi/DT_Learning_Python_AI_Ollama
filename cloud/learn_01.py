# **************************************************
# Step (1)
# **************************************************
# https://docs.ollama.com
#
# https://ollama.com/cloud
# https://docs.ollama.com/cloud
#
# https://ollama.com/settings/keys
# **************************************************
# glm-4.6:cloud
# kimi-k2:1t-cloud
# minimax-m2:cloud
# gpt-oss:20b-cloud
# gpt-oss:120b-cloud
# qwen3-coder:480b-cloud
# deepseek-v3.1:671b-cloud
# **************************************************


# **************************************************
# import os
# from ollama import Client
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv(key="OLLAMA_API_KEY")

# if not api_key:
#     print(f"[-] Key not found or is empty!")
#     exit()

# client = Client(
#     host="https://ollama.com",
#     headers={"Authorization": f"Bearer {api_key}"},
# )

# response = client.chat(
#     model="gpt-oss:20b-cloud",
#     messages=[{"role": "user", "content": "Tell me a joke."}],
# )

# print(response.message.content)
# **************************************************


# **************************************************
# googooli> my_module.py
# googooli> app.py
#
# app.py:
# import my_module
# **************************************************


# **************************************************
# googooli> my_module.py
# googooli\magooli> app.py
#
# app.py:
# import my_module -> Error!
# **************************************************


# **************************************************
# googooli> my_module.py
# googooli\magooli> app.py
#
# app.py:
# import sys
# sys.path.append("..")
# import my_module -> OK
# **************************************************


# **************************************************
# - Constants
# - temperature
# - How to import your module from parent directory!
# **************************************************
import sys

sys.path.append("..")

import os
from rich import print
from ollama import Client
from dtx_dotenv import get_key_value

TEMPERATURE: float = 0.7
BASE_URL: str = "https://ollama.com".strip().lower()
MODEL_NAME: str = "gpt-oss:20b-cloud".strip().lower()
KEY_NAME_OLLAMA_API_KEY: str = "OLLAMA_API_KEY".strip().upper()

os.system(command="cls" if os.name == "nt" else "clear")

api_key: str = get_key_value(
    key=KEY_NAME_OLLAMA_API_KEY,
)

headers: dict = {"Authorization": f"Bearer {api_key}"}

client = Client(
    host=BASE_URL,
    headers=headers,
)

messages: list[dict] = []

user_prompt: str = "Tell me a joke."
user_message: dict = {"role": "user", "content": user_prompt}
messages.append(user_message)

response = client.chat(
    model=MODEL_NAME,
    messages=messages,
    options={"temperature": TEMPERATURE},
)

assistant_answer: str | None = response.message.content

print("=" * 50)
print(assistant_answer)
print("=" * 50)
# **************************************************


# **************************************************
# - System Prompt
# - Simpole Chatbot
# - Without History
# **************************************************
# import sys

# sys.path.append("..")

# import os
# from rich import print
# from ollama import Client
# from dtx_dotenv import get_key_value

# TEMPERATURE: float = 0.7
# BASE_URL: str = "https://ollama.com".strip().lower()
# MODEL_NAME: str = "gpt-oss:20b-cloud".strip().lower()
# KEY_NAME_OLLAMA_API_KEY: str = "OLLAMA_API_KEY".strip().upper()

# SYSTEM_PROMPT: str = "You are a helpful AI assistant."
# SYSTEM_MESSAGE: dict = {"role": "system", "content": SYSTEM_PROMPT}

# os.system(command="cls" if os.name == "nt" else "clear")

# while True:
#     print("=" * 50)
#     user_prompt: str = input("User: ").strip()

#     if user_prompt.lower() in ["bye", "exit", "quit"]:
#         break

#     api_key: str = get_key_value(
#         key=KEY_NAME_OLLAMA_API_KEY,
#     )

#     headers: dict = {"Authorization": f"Bearer {api_key}"}

#     client = Client(
#         host=BASE_URL,
#         headers=headers,
#     )

#     messages: list[dict] = []
#     messages.append(SYSTEM_MESSAGE)

#     user_message: dict = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     response = client.chat(
#         model=MODEL_NAME,
#         messages=messages,
#         options={"temperature": TEMPERATURE},
#     )

#     print("-" * 50)
#     print(response.message.content)
#     print("=" * 50)
#     print()
# **************************************************
