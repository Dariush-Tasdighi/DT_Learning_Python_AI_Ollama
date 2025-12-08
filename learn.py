# **************************************************
# Step (1)
# **************************************************
# import ollama

# print("=" * 50)
# # همان‌طور که قبلا گفتم، دستور ذیل، همیشه کار نمی‌کند
# print(f"Version of Ollama: {ollama.__version__}")
# print("=" * 50)
# **************************************************


# **************************************************
# Step (2) - 'generate()' method
# **************************************************
import ollama

generate_completion = ollama.generate(
    model="gemma3:1b",
    prompt="Tell me a joke.",
)

print("=" * 50)
print(generate_completion)
print("-" * 50)
print(generate_completion.response)
print("=" * 50)
# **************************************************


# **************************************************
# Step (3) - Using 'rich' package
# **************************************************
# import ollama
# # NEW
# from rich import print

# generate_completion = ollama.generate(
#     model="gemma3:1b",
#     prompt="Tell me a joke.",
# )

# print("=" * 50)
# print(generate_completion)
# print("-" * 50)
# print(generate_completion.response)
# print("=" * 50)
# **************************************************


# **************************************************
# Step (4) - 'chat()' method
# **************************************************
# import ollama
# from rich import print

# # NEW
# response = ollama.chat(
#     model="gemma3:1b",
#     messages=[{"role": "user", "content": "Tell me a joke."}],
# )

# print("=" * 50)
# print(response)
# print("=" * 50)
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# 'response'
# **************************************************
# ChatResponse(
#     model='gemma3:1b',
#     created_at='2025-08-17T12:31:24.4620909Z',
#     done=True,
#     done_reason='stop',
#     total_duration=1061336000,
#     load_duration=89586200,
#     prompt_eval_count=14,
#     prompt_eval_duration=258898600,
#     eval_count=45,
#     eval_duration=712221900,
#     message=Message(
#         role='assistant',
#         content='Why did the square cross quit its job? ...
#         thinking=None,
#         images=None,
#         tool_name=None,
#         tool_calls=None
#     )
# )
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# Step (5)
# **************************************************
# # NEW
# import os
# import ollama
# from rich import print

# # NEW: لوس‌بازی
# from ollama import ChatResponse

# # NEW: Constant
# MODEL_NAME: str = "gemma3:1b".strip().lower()

# # NEW
# os.system(command="cls" if os.name == "nt" else "clear")

# # NEW
# messages: list[dict] = []

# # NEW
# user_prompt: str = "Tell me a joke."
# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# # NEW: ChatResponse
# response: ChatResponse = ollama.chat(
#     model=MODEL_NAME,
#     messages=messages,
# )

# print("=" * 50)
# # NEW:‌ ‌Best Practice
# print(response.message.content)
# print("-" * 50)
# # NEW: Bad Practice
# print(response["message"]["content"])
# print("=" * 50)
# **************************************************


# **************************************************
# Step (6) - Client
# **************************************************
# import os
# from rich import print
# from ollama import ChatResponse

# # NEW
# from ollama import Client

# MODEL_NAME: str = "gemma3:1b".strip().lower()

# # NEW
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()
# # BASE_URL: str = "http://localhost:11434".strip().lower()

# os.system(command="cls" if os.name == "nt" else "clear")

# messages: list[dict] = []

# # NEW
# user_prompt: str = "Tell me a short science fiction story."
# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# # NEW
# client = Client(
#     host=BASE_URL,
# )

# response: ChatResponse = client.chat(
#     # NEW
#     stream=False,  # Default: False
#     model=MODEL_NAME,
#     messages=messages,
# )

# print("=" * 50)
# print(response.message.content)
# print("=" * 50)
# **************************************************


# **************************************************
# Step (7) - 'rich': Markdown
# **************************************************
# import os
# from rich import print
# from ollama import Client
# from ollama import ChatResponse

# # NEW
# from rich.console import Console
# from rich.markdown import Markdown

# MODEL_NAME: str = "gemma3:1b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# os.system(command="cls" if os.name == "nt" else "clear")

# messages: list[dict] = []

# # NEW
# # user_prompt: str = "Tell me a short science fiction story."
# user_prompt: str = "Write a python code to print numbers between one to ten."

# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(
#     host=BASE_URL,
# )

# response: ChatResponse = client.chat(
#     stream=False,
#     model=MODEL_NAME,
#     messages=messages,
# )

# assistant_answer: str | None = response.message.content

# if not assistant_answer:
#     assistant_answer = "[-] No content received!"

# print("=" * 50)
# # print(assistant_answer)
# # NEW
# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)
# print("=" * 50)
# **************************************************


# **************************************************
# Step (8) - Temperature
# **************************************************
# import os
# from rich import print
# from ollama import Client
# from ollama import ChatResponse
# from rich.console import Console
# from rich.markdown import Markdown

# # NEW
# TEMPERATURE: float = 0.7

# MODEL_NAME: str = "gemma3:1b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# os.system(command="cls" if os.name == "nt" else "clear")

# messages: list[dict] = []

# user_prompt: str = "Tell me a long science fiction story."
# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(
#     host=BASE_URL,
# )

# response: ChatResponse = client.chat(
#     stream=False,
#     model=MODEL_NAME,
#     messages=messages,
#     # NEW
#     options={"temperature": TEMPERATURE},
# )

# assistant_answer: str | None = response.message.content

# if not assistant_answer:
#     assistant_answer = "[-] No content received!"

# print("=" * 50)
# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)
# print("=" * 50)
# **************************************************


# **************************************************
# Step (9) - Stream
# **************************************************
# import os
# from rich import print
# from ollama import Client
# from ollama import ChatResponse

# # from rich.console import Console
# # from rich.markdown import Markdown

# # NEW
# from typing import Iterator

# TEMPERATURE: float = 0.7
# MODEL_NAME: str = "gemma3:1b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# os.system(command="cls" if os.name == "nt" else "clear")

# messages: list[dict] = []

# user_prompt: str = "Tell me a long science fiction story."
# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(
#     host=BASE_URL,
# )

# # NEW: ChatResponse -> Iterator[ChatResponse]
# response_stream: Iterator[ChatResponse] = client.chat(
#     # NEW
#     stream=True,
#     model=MODEL_NAME,
#     messages=messages,
#     options={"temperature": TEMPERATURE},
# )

# print("=" * 50)
# # NEW
# for chunk in response_stream:
#     content: str | None = chunk.message.content
#     if content:
#         print(content, end="", flush=True)
# print("=" * 50)
# **************************************************


# **************************************************
# Step (10) - Response Time
# **************************************************
# import os
# from rich import print
# from ollama import Client
# from ollama import ChatResponse
# from rich.console import Console
# from rich.markdown import Markdown

# # NEW
# import time

# TEMPERATURE: float = 0.7
# MODEL_NAME: str = "gemma3:1b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# os.system(command="cls" if os.name == "nt" else "clear")

# messages: list[dict] = []

# user_prompt: str = "Tell me a short science fiction story."
# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(
#     host=BASE_URL,
# )

# # NEW
# start_time: float = time.time()

# response: ChatResponse = client.chat(
#     stream=False,
#     model=MODEL_NAME,
#     messages=messages,
#     options={"temperature": TEMPERATURE},
# )

# # NEW
# response_time: float = time.time() - start_time

# assistant_answer: str | None = response.message.content

# if not assistant_answer:
#     assistant_answer = "[-] No content received!"

# print("=" * 50)
# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)
# print("-" * 50)
# # NEW
# print(f"Full response received {response_time:.2f} seconds after request.")
# print("=" * 50)
# **************************************************


# **************************************************
# Step (11) - Reasoning - Thinking
# **************************************************
# import os
# import time
# from rich import print
# from ollama import Client
# from ollama import ChatResponse
# from rich.console import Console
# from rich.markdown import Markdown

# TEMPERATURE: float = 0.7
# # NEW
# MODEL_NAME: str = "deepseek-r1:1.5b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# os.system(command="cls" if os.name == "nt" else "clear")

# messages: list[dict] = []

# user_prompt: str = (
#     "If it takes one hour for a pair of pants to dry on the rooftop, how long will it take for ten pairs of pants to dry on the rooftop?"
# )
# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(
#     host=BASE_URL,
# )

# start_time: float = time.time()

# response: ChatResponse = client.chat(
#     # NEW
#     think=True,
#     # think=False,  # Default: False
#     stream=False,
#     model=MODEL_NAME,
#     messages=messages,
#     options={"temperature": TEMPERATURE},
# )

# response_time: float = time.time() - start_time

# assistant_answer: str | None = response.message.content

# if not assistant_answer:
#     assistant_answer = "[-] No content received!"

# assistant_thinking: str | None = response.message.thinking

# if not assistant_thinking:
#     assistant_thinking = "[-] No thinking received!"

# print("=" * 50)
# print(response)
# print("-" * 50)
# # NEW
# console = Console()
# markdown = Markdown(markup=assistant_thinking)
# console.print(markdown)
# print("-" * 50)
# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)
# print("-" * 50)
# print(f"Full response received {response_time:.2f} seconds after request.")
# print("=" * 50)
# **************************************************


# **************************************************
# response
# **************************************************
# model='deepseek-r1:1.5b'
# created_at='2025-07-21T18:09:57.8372849Z'
# done=True
# done_reason='stop'
# total_duration=10002141100
# load_duration=58904100
# prompt_eval_count=35
# prompt_eval_duration=32075000
# eval_count=325
# eval_duration=9910608100
# message=Message(
#   role='assistant',
#   content="**Solution:**\n\nTo determine how long it will take for ten pairs of pants to dry on the rooftop...",
#   thinking="First, I need to determine how long it takes for a single pair of pants to dry. The problem...",
#   images=None,
#   tool_calls=None
# )
# **************************************************


# **************************************************
# Step (12)
# **************************************************
# - Without History
# - Simple Text Chat Bot
# - System Prompt -> System Message
# **************************************************
# import os
# import time
# from rich import print
# from ollama import Client
# from ollama import ChatResponse
# from rich.console import Console
# from rich.markdown import Markdown

# TEMPERATURE: float = 0.7
# # NEW
# # MODEL_NAME: str = "gemma3:1b".strip().lower()
# MODEL_NAME: str = "llama3.2:1b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# # NEW
# SYSTEM_PROMPT: str = "You are a helpful AI assistant."
# SYSTEM_MESSAGE: dict = {"role": "system", "content": SYSTEM_PROMPT}

# os.system(command="cls" if os.name == "nt" else "clear")

# # NEW
# while True:
#     print("=" * 50)
#     user_prompt: str = input("User: ").strip()

#     if user_prompt.lower() in ["bye", "exit", "quit"]:
#         break

#     messages: list[dict] = []
#     messages.append(SYSTEM_MESSAGE)

#     user_message: dict = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     client = Client(
#         host=BASE_URL,
#     )

#     start_time: float = time.time()

#     response: ChatResponse = client.chat(
#         think=False,
#         stream=False,
#         model=MODEL_NAME,
#         messages=messages,
#         options={"temperature": TEMPERATURE},
#     )

#     response_time: float = time.time() - start_time

#     assistant_answer: str | None = response.message.content

#     if not assistant_answer:
#         assistant_answer = "[-] No content received!"

#     print("-" * 50)
#     console = Console()
#     markdown = Markdown(markup=assistant_answer)
#     console.print(markdown)
#     print("-" * 50)
#     print(f"Full response received {response_time:.2f} seconds after request.")
#     print("=" * 50)
#     print()
# **************************************************


# **************************************************
# Step (13)
# **************************************************
# - With History
# - Simple Text Chat Bot
# - System Prompt -> System Message
# **************************************************
# import os
# import time
# from rich import print
# from ollama import Client
# from ollama import ChatResponse
# from rich.console import Console
# from rich.markdown import Markdown

# TEMPERATURE: float = 0.7
# # MODEL_NAME: str = "gemma3:1b".strip().lower()
# MODEL_NAME: str = "llama3.2:1b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# SYSTEM_PROMPT: str = "You are a helpful AI assistant."
# SYSTEM_MESSAGE: dict = {"role": "system", "content": SYSTEM_PROMPT}

# os.system(command="cls" if os.name == "nt" else "clear")

# # NEW
# messages: list[dict] = []
# messages.append(SYSTEM_MESSAGE)

# while True:
#     print("=" * 50)
#     user_prompt: str = input("User: ").strip()

#     if user_prompt.lower() in ["bye", "exit", "quit"]:
#         break

#     user_message: dict = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     client = Client(
#         host=BASE_URL,
#     )

#     start_time: float = time.time()

#     response: ChatResponse = client.chat(
#         think=False,
#         stream=False,
#         model=MODEL_NAME,
#         messages=messages,
#         options={"temperature": TEMPERATURE},
#     )

#     response_time: float = time.time() - start_time

#     #در این مثال، فرض بر این است که حتما جواب داریم
#     assistant_answer: str | None = response.message.content

#     if not assistant_answer:
#         assistant_answer = "[-] No content received!"

#     # NEW
#     assistant_message: dict = {"role": "assistant", "content": assistant_answer}
#     messages.append(assistant_message)

#     print("-" * 50)
#     console = Console()
#     markdown = Markdown(markup=assistant_answer)
#     console.print(markdown)
#     print("-" * 50)
#     print(f"Full response received {response_time:.2f} seconds after request.")
#     print("=" * 50)
#     print()
# **************************************************


# **************************************************
# Step (14) - Best Practice (1)
# **************************************************
# import os
# import time
# from rich import print
# from ollama import Client
# from ollama import ChatResponse
# from rich.console import Console
# from rich.markdown import Markdown

# # NEW
# USER_QUESTION: str = "User: "
# EXIT_COMMANDS: list[str] = [
#     "bye".strip().lower(),
#     "exit".strip().lower(),
#     "quit".strip().lower(),
# ]

# # NEW
# KEY_NAME_ROLE = "role".strip().lower()
# KEY_NAME_CONTENT = "content".strip().lower()
# KEY_NAME_TEMPRETURE = "temperature".strip().lower()

# # NEW
# ROLE_USER: str = "user".strip().lower()
# ROLE_SYSTEM: str = "system".strip().lower()
# ROLE_ASSISTANT: str = "assistant".strip().lower()

# TEMPERATURE: float = 0.7
# # MODEL_NAME: str = "gemma3:1b".strip().lower()
# MODEL_NAME: str = "llama3.2:1b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# SYSTEM_PROMPT: str = "You are a helpful AI assistant."

# # NEW
# SYSTEM_MESSAGE: dict = {
#     KEY_NAME_ROLE: ROLE_SYSTEM,
#     KEY_NAME_CONTENT: SYSTEM_PROMPT,
# }

# os.system(command="cls" if os.name == "nt" else "clear")

# messages: list[dict] = []
# messages.append(SYSTEM_MESSAGE)

# while True:
#     print("=" * 50)
#     # NEW
#     user_prompt: str = input(USER_QUESTION).strip()

#     # NEW
#     if user_prompt.lower() in EXIT_COMMANDS:
#         break

#     # NEW
#     user_message: dict = {
#         KEY_NAME_ROLE: ROLE_USER,
#         KEY_NAME_CONTENT: user_prompt,
#     }
#     messages.append(user_message)

#     client = Client(
#         host=BASE_URL,
#     )

#     start_time: float = time.time()

#     response: ChatResponse = client.chat(
#         think=False,
#         stream=False,
#         messages=messages,
#         model=MODEL_NAME,
#         options={KEY_NAME_TEMPRETURE: TEMPERATURE},
#     )

#     response_time: float = time.time() - start_time

#     assistant_answer: str | None = response.message.content

#     if not assistant_answer:
#         assistant_answer = "[-] No content received!"

#     # NEW
#     assistant_message: dict = {
#         KEY_NAME_ROLE: ROLE_ASSISTANT,
#         KEY_NAME_CONTENT: assistant_answer,
#     }
#     messages.append(assistant_message)

#     print("-" * 50)
#     console = Console()
#     markdown = Markdown(markup=assistant_answer)
#     console.print(markdown)
#     print("-" * 50)
#     print(f"Full response received {response_time:.2f} seconds after request.")
#     print("=" * 50)
#     print()
# **************************************************


# **************************************************
# Step (15) - Best Practice (2)
# **************************************************
# import os
# import time
# from rich import print
# from ollama import Client
# from ollama import ChatResponse
# from rich.console import Console
# from rich.markdown import Markdown

# EXIT_COMMANDS: list[str] = [
#     "bye".strip().lower(),
#     "exit".strip().lower(),
#     "quit".strip().lower(),
# ]

# USER_QUESTION: str = "User: "
# # NEW
# MESSAGE_NO_CONTENT_RECEIVED: str = "[-] No content received!"

# KEY_NAME_ROLE = "role".strip().lower()
# KEY_NAME_CONTENT = "content".strip().lower()
# KEY_NAME_TEMPRETURE = "temperature".strip().lower()

# ROLE_USER: str = "user".strip().lower()
# ROLE_SYSTEM: str = "system".strip().lower()
# ROLE_ASSISTANT: str = "assistant".strip().lower()

# TEMPERATURE: float = 0.7
# # MODEL_NAME: str = "gemma3:1b".strip().lower()
# MODEL_NAME: str = "llama3.2:1b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# SYSTEM_PROMPT: str = "You are a helpful AI assistant."

# SYSTEM_MESSAGE: dict = {
#     KEY_NAME_ROLE: ROLE_SYSTEM,
#     KEY_NAME_CONTENT: SYSTEM_PROMPT,
# }


# # NEW
# def chat(
#     messages: list[dict],
#     think: bool = False,
#     base_url: str = BASE_URL,
#     model_name: str = MODEL_NAME,
#     temperature: float = TEMPERATURE,
# ) -> str | None:
#     """Chat with Ollama service."""

#     client = Client(
#         host=base_url,
#     )

#     response: ChatResponse = client.chat(
#         think=think,
#         stream=False,
#         model=model_name,
#         messages=messages,
#         options={KEY_NAME_TEMPRETURE: temperature},
#     )

#     assistant_answer: str | None = response.message.content

#     return assistant_answer


# # NEW
# def main() -> None:
#     """The main of program"""

#     os.system(command="cls" if os.name == "nt" else "clear")

#     messages: list[dict] = []
#     messages.append(SYSTEM_MESSAGE)

#     while True:
#         print("=" * 50)
#         user_prompt: str = input(USER_QUESTION).strip()

#         if user_prompt.lower() in EXIT_COMMANDS:
#             break

#         user_message: dict = {
#             KEY_NAME_ROLE: ROLE_USER,
#             KEY_NAME_CONTENT: user_prompt,
#         }
#         messages.append(user_message)

#         start_time: float = time.time()

#         assistant_answer: str | None = chat(
#             messages=messages,
#         )

#         response_time: float = time.time() - start_time

#         # NEW
#         if not assistant_answer:
#             messages.pop()
#             assistant_answer = MESSAGE_NO_CONTENT_RECEIVED
#         else:
#             assistant_message: dict = {
#                 KEY_NAME_ROLE: ROLE_ASSISTANT,
#                 KEY_NAME_CONTENT: assistant_answer,
#             }
#             messages.append(assistant_message)

#         print("-" * 50)
#         console = Console()
#         markdown = Markdown(markup=assistant_answer)
#         console.print(markdown)
#         print("-" * 50)
#         print(f"Full response received {response_time:.2f} seconds after request.")
#         print("=" * 50)
#         print()


# # NEW
# if __name__ == "__main__":
#     main()
# **************************************************
# messages:

# System Message
# User Message 1
# Assistant Message 1
# User Message 2
# Assistant Message 2
# User Message 3
#   Assistant Answer: None OR "" -> messages.pop()

# =>

# messages:

# System Message
# User Message 1
# Assistant Message 1
# User Message 2
# Assistant Message 2
# **************************************************


# **************************************************
# Step (16) - Best Practice (2) - KeyboardInterrupt
# **************************************************
# import os
# import time
# from rich import print
# from ollama import Client
# from ollama import ChatResponse
# from rich.console import Console
# from rich.markdown import Markdown

# EXIT_COMMANDS: list[str] = [
#     "bye".strip().lower(),
#     "exit".strip().lower(),
#     "quit".strip().lower(),
# ]

# USER_QUESTION: str = "User: "
# MESSAGE_NO_CONTENT_RECEIVED: str = "[-] No content received!"

# KEY_NAME_ROLE = "role".strip().lower()
# KEY_NAME_CONTENT = "content".strip().lower()
# KEY_NAME_TEMPRETURE = "temperature".strip().lower()

# ROLE_USER: str = "user".strip().lower()
# ROLE_SYSTEM: str = "system".strip().lower()
# ROLE_ASSISTANT: str = "assistant".strip().lower()

# TEMPERATURE: float = 0.7
# # MODEL_NAME: str = "gemma3:1b".strip().lower()
# MODEL_NAME: str = "llama3.2:1b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# SYSTEM_PROMPT: str = "You are a helpful AI assistant."

# SYSTEM_MESSAGE: dict = {
#     KEY_NAME_ROLE: ROLE_SYSTEM,
#     KEY_NAME_CONTENT: SYSTEM_PROMPT,
# }


# def chat(
#     messages: list[dict],
#     think: bool = False,
#     base_url: str = BASE_URL,
#     model_name: str = MODEL_NAME,
#     temperature: float = TEMPERATURE,
# ) -> str | None:
#     """Chat with Ollama service."""

#     client = Client(
#         host=base_url,
#     )

#     response: ChatResponse = client.chat(
#         think=think,
#         stream=False,
#         model=model_name,
#         messages=messages,
#         options={KEY_NAME_TEMPRETURE: temperature},
#     )

#     assistant_answer: str | None = response.message.content

#     return assistant_answer


# def main() -> None:
#     """The main of program"""

#     os.system(command="cls" if os.name == "nt" else "clear")

#     messages: list[dict] = []
#     messages.append(SYSTEM_MESSAGE)

#     while True:
#         print("=" * 50)
#         user_prompt: str = input(USER_QUESTION).strip()

#         if user_prompt.lower() in EXIT_COMMANDS:
#             break

#         user_message: dict = {
#             KEY_NAME_ROLE: ROLE_USER,
#             KEY_NAME_CONTENT: user_prompt,
#         }
#         messages.append(user_message)

#         start_time: float = time.time()

#         assistant_answer: str | None = chat(
#             messages=messages,
#         )

#         response_time: float = time.time() - start_time

#         if not assistant_answer:
#             messages.pop()
#             assistant_answer = MESSAGE_NO_CONTENT_RECEIVED
#         else:
#             assistant_message: dict = {
#                 KEY_NAME_ROLE: ROLE_ASSISTANT,
#                 KEY_NAME_CONTENT: assistant_answer,
#             }
#             messages.append(assistant_message)

#         print("-" * 50)
#         console = Console()
#         markdown = Markdown(markup=assistant_answer)
#         console.print(markdown)
#         print("-" * 50)
#         print(f"Full response received {response_time:.2f} seconds after request.")
#         print("=" * 50)
#         print()


# if __name__ == "__main__":
#     # NEW
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as error:
#         # Log 'error'
#         print(f"[-] {error}!")

#     print()
# **************************************************


# **************************************************
# Step (17) - Best Practice (3) - Calculate Input / Output Tokens
# **************************************************
# import os
# import time
# from rich import print
# from ollama import Client
# from ollama import ChatResponse
# from rich.console import Console
# from rich.markdown import Markdown

# EXIT_COMMANDS: list[str] = [
#     "bye".strip().lower(),
#     "exit".strip().lower(),
#     "quit".strip().lower(),
# ]

# USER_QUESTION: str = "User: "
# MESSAGE_NO_CONTENT_RECEIVED: str = "[-] No content received!"

# KEY_NAME_ROLE = "role".strip().lower()
# KEY_NAME_CONTENT = "content".strip().lower()
# KEY_NAME_TEMPRETURE = "temperature".strip().lower()

# ROLE_USER: str = "user".strip().lower()
# ROLE_SYSTEM: str = "system".strip().lower()
# ROLE_ASSISTANT: str = "assistant".strip().lower()

# TEMPERATURE: float = 0.7
# # MODEL_NAME: str = "gemma3:1b".strip().lower()
# MODEL_NAME: str = "llama3.2:1b".strip().lower()
# BASE_URL: str = "http://127.0.0.1:11434".strip().lower()

# SYSTEM_PROMPT: str = "You are a helpful AI assistant."

# SYSTEM_MESSAGE: dict = {
#     KEY_NAME_ROLE: ROLE_SYSTEM,
#     KEY_NAME_CONTENT: SYSTEM_PROMPT,
# }


# def chat(
#     messages: list[dict],
#     think: bool = False,
#     # NEW
#     notify: bool = False,
#     base_url: str = BASE_URL,
#     model_name: str = MODEL_NAME,
#     temperature: float = TEMPERATURE,
# ) -> tuple[str | None, int, int]:
#     """Chat with Ollama service."""

#     client = Client(
#         host=base_url,
#     )

#     # NEW
#     if notify:
#         print(f"Ollama chat started ({model_name})...")

#     response: ChatResponse = client.chat(
#         think=think,
#         stream=False,
#         model=model_name,
#         messages=messages,
#         options={KEY_NAME_TEMPRETURE: temperature},
#     )

#     # NEW
#     if notify:
#         print(f"Ollama chat finished ({model_name}).")

#     assistant_answer: str | None = response.message.content

#     prompt_tokens: int = 0
#     completion_tokens: int = 0

#     if assistant_answer:
#         if response.eval_count:
#             completion_tokens = response.eval_count
#         if response.prompt_eval_count:
#             prompt_tokens = response.prompt_eval_count

#     return assistant_answer, prompt_tokens, completion_tokens


# def main() -> None:
#     """The main of program"""

#     os.system(command="cls" if os.name == "nt" else "clear")

#     messages: list[dict] = []
#     messages.append(SYSTEM_MESSAGE)

#     while True:
#         print("=" * 50)
#         user_prompt: str = input(USER_QUESTION).strip()

#         if user_prompt.lower() in EXIT_COMMANDS:
#             break

#         user_message: dict = {
#             KEY_NAME_ROLE: ROLE_USER,
#             KEY_NAME_CONTENT: user_prompt,
#         }
#         messages.append(user_message)

#         start_time: float = time.time()

#         # NEW
#         # assistant_answer, _, _ = chat(
#         #     messages=messages,
#         # )

#         # NEW
#         assistant_answer, prompt_tokens, completion_tokens = chat(
#             messages=messages,
#         )

#         response_time: float = time.time() - start_time

#         if not assistant_answer:
#             messages.pop()
#             assistant_answer = MESSAGE_NO_CONTENT_RECEIVED
#         else:
#             assistant_message: dict = {
#                 KEY_NAME_ROLE: ROLE_ASSISTANT,
#                 KEY_NAME_CONTENT: assistant_answer,
#             }
#             messages.append(assistant_message)

#         print("-" * 50)
#         console = Console()
#         markdown = Markdown(markup=assistant_answer)
#         console.print(markdown)
#         print("-" * 50)
#         # NEW
#         print("Prompt Tokens (Input):", prompt_tokens)
#         print("-" * 50)
#         # NEW
#         print("Completion Tokens (Output):", completion_tokens)
#         print("-" * 50)
#         print(f"Full response received {response_time:.2f} seconds after request.")
#         print("=" * 50)
#         print()


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as error:
#         # Log 'error'
#         print(f"[-] {error}!")

#     print()
# **************************************************
