# **************************************************
# Step (1)
# **************************************************
import ollama

from rich import print
from dt_utility import clear_screen

clear_screen()

print("=" * 50)
# همان‌طور که قبلا گفتم، دستور ذیل، همیشه کار نمی‌کند
# print(f"Version of 'ollama' package: {ollama.__version__}")
print("=" * 50)
print()
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# In Windows PowerShell (Run as administrator)
#
# > Get-ChildItem Env:
#
# > Get-ChildItem Env:TEMP
#
# > Get-ChildItem Env:OLLAMA_MODELS
#       Cannot find path 'OLLAMA_MODELS' because it does not exist.
#
# > [System.Environment]::SetEnvironmentVariable("OLLAMA_MODELS", "D:\OLLAMA_MODELS", "Machine")
#
# > Get-ChildItem Env:OLLAMA_MODELS
#       Cannot find path 'OLLAMA_MODELS' because it does not exist.
#
# # Close Windows PowerShell and Open Again!
#
# > Get-ChildItem Env:OLLAMA_MODELS
#       Name                           Value
#       ----                           -----
#       OLLAMA_MODELS                  D:\OLLAMA_MODELS
#
# > [System.Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "Machine")
#       D:\OLLAMA_MODELS
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# Step (2) - 'generate()' method
# **************************************************
# Error: ConnectionError: Failed to connect to Ollama.
# Please check that Ollama is downloaded, running and
# accessible. https://ollama.com/download
#
# > ollama start
# > ollama serve
# **************************************************
# import ollama

# from rich import print
# from dt_utility import clear_screen

# clear_screen()

# generate_completion = ollama.generate(
#     model="gemma3:1b",
#     prompt="Tell me a joke.",
# )

# print("=" * 50)
# print(generate_completion)
# print("-" * 50)
# print(generate_completion.response)
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (3) - 'chat()' method
# **************************************************
# import ollama

# from rich import print
# from dt_utility import clear_screen

# clear_screen()

# # NEW: 'generate()' -> 'chat()'
# response = ollama.chat(
#     model="gemma3:1b",
#     messages=[{"role": "user", "content": "Tell me a joke."}],
# )

# print("=" * 50)
# print(response)
# print("=" * 50)
# print()
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
# Step (4)
# **************************************************
# import ollama

# from rich import print
# from typing import Final
# from dt_utility import clear_screen

# # NEW: لوس‌بازی
# from ollama import ChatResponse

# # NEW
# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()

# clear_screen()

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
# print()
# **************************************************


# **************************************************
# Step (5) - Client
# **************************************************
# from rich import print
# from typing import Final
# from ollama import ChatResponse
# from dt_utility import clear_screen

# # NEW
# # import ollama
# from ollama import Client

# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()

# # NEW
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()
# # BASE_URL: Final[str] = "http://localhost:11434".replace(" ", "").lower()

# clear_screen()

# messages: list[dict] = []

# # NEW: Change 'user_prompt' value
# user_prompt: str = "Tell me a short science fiction story."

# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# # NEW
# client = Client(host=BASE_URL)

# response: ChatResponse = client.chat(
#     # NEW
#     stream=False,  # Default: False
#     #
#     model=MODEL_NAME,
#     messages=messages,
# )

# print("=" * 50)
# print(response.message.content)
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (6) - 'rich': Markdown
# **************************************************
# from rich import print
# from typing import Final
# from ollama import Client
# from ollama import ChatResponse
# from dt_utility import clear_screen

# # NEW
# from typing import Optional
# from rich.console import Console
# from rich.markdown import Markdown

# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# clear_screen()

# messages: list[dict] = []

# # NEW: Change 'user_prompt' value
# user_prompt: str = "Write a python code to print numbers between one to ten."

# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(host=BASE_URL)

# response: ChatResponse = client.chat(
#     stream=False,
#     model=MODEL_NAME,
#     messages=messages,
# )

# # NEW
# # assistant_answer: str | None = response.message.content
# assistant_answer: Optional[str] = response.message.content

# # NEW
# if not assistant_answer:
#     assistant_answer = "[red][bold][-][/bold] No content received![/red]"

# print("=" * 50)
# # NEW
# print(assistant_answer)
# # console = Console()
# # markdown = Markdown(markup=assistant_answer)
# # console.print(markdown)
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (7) - Temperature
# **************************************************
# from typing import Final
# from typing import Optional

# from ollama import Client
# from ollama import ChatResponse

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# from dt_utility import clear_screen

# # NEW
# TEMPERATURE: Final[float] = 0.7

# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# clear_screen()

# messages: list[dict] = []

# # NEW: Change 'user_prompt' value
# user_prompt: str = "Tell me a long science fiction story."

# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(host=BASE_URL)

# response: ChatResponse = client.chat(
#     stream=False,
#     model=MODEL_NAME,
#     messages=messages,
#     # NEW
#     options={"temperature": TEMPERATURE},
# )

# assistant_answer: Optional[str] = response.message.content

# if not assistant_answer:
#     assistant_answer = "[red][bold][-][/bold] No content received![/red]"

# print("=" * 50)
# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (8) - Stream
# **************************************************
# from typing import Final
# from typing import Optional

# from rich import print

# from ollama import Client
# from ollama import ChatResponse

# from dt_utility import clear_screen

# # NEW
# from typing import Iterator

# TEMPERATURE: Final[float] = 0.7
# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# clear_screen()

# messages: list[dict] = []

# user_prompt: str = "Tell me a long science fiction story."
# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(host=BASE_URL)

# # NEW: ChatResponse -> Iterator[ChatResponse]
# response_stream: Iterator[ChatResponse] = client.chat(
#     # NEW
#     stream=True,
#     #
#     model=MODEL_NAME,
#     messages=messages,
#     options={"temperature": TEMPERATURE},
# )

# print("=" * 50)
# # NEW
# for chunk in response_stream:
#     content: Optional[str] = chunk.message.content
#     if content:
#         print(content, end="", flush=True)
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (9) - Elapsed Time
# **************************************************
# from typing import Final
# from typing import Optional

# from ollama import Client
# from ollama import ChatResponse

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# from dt_utility import clear_screen

# # NEW
# import time

# TEMPERATURE: Final[float] = 0.7
# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# clear_screen()

# messages: list[dict] = []

# # NEW: Change 'user_prompt' value
# user_prompt: str = "Tell me a joke."

# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(host=BASE_URL)

# # NEW
# start_time: float = time.time()

# response: ChatResponse = client.chat(
#     stream=False,
#     model=MODEL_NAME,
#     messages=messages,
#     options={"temperature": TEMPERATURE},
# )

# # NEW
# end_time: float = time.time()
# elapsed_time: float = end_time - start_time

# assistant_answer: Optional[str] = response.message.content

# if not assistant_answer:
#     assistant_answer = "[red][bold][-][/bold] No content received![/red]"

# print("=" * 50)
# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)

# # NEW
# print("-" * 50)
# print(f"Elapsed Time: {elapsed_time:.2f} second(s).")

# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (10) - Elapsed Time with 'perf_counter()'
# **************************************************
# import time

# from typing import Final
# from typing import Optional

# from ollama import Client
# from ollama import ChatResponse

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# from dt_utility import clear_screen

# # NEW
# from dt_utility import format_seconds

# TEMPERATURE: Final[float] = 0.7
# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# clear_screen()

# messages: list[dict] = []

# user_prompt: str = "Tell me a joke."
# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(host=BASE_URL)

# # NEW
# # start_time: float = time.time()
# start_time: float = time.perf_counter()

# response: ChatResponse = client.chat(
#     stream=False,
#     model=MODEL_NAME,
#     messages=messages,
#     options={"temperature": TEMPERATURE},
# )

# # NEW
# # end_time: float = time.time()
# # elapsed_time: float = end_time - start_time
# end_time: float = time.perf_counter()
# elapsed_time: float = end_time - start_time
# formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

# assistant_answer: Optional[str] = response.message.content

# if not assistant_answer:
#     assistant_answer = "[red][bold][-][/bold] No content received![/red]"

# print("=" * 50)
# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)
# print("-" * 50)
# # NEW
# # print(f"Elapsed Time: {elapsed_time:.2f} second(s).")
# print(f"Elapsed Time: {formatted_elapsed_time}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (11) - Reasoning - Thinking
# **************************************************
# import time

# from typing import Final
# from typing import Optional

# from ollama import Client
# from ollama import ChatResponse

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# from dt_utility import clear_screen
# from dt_utility import format_seconds

# TEMPERATURE: Final[float] = 0.7
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# # NEW
# MODEL_NAME: Final[str] = "deepseek-r1:1.5b".replace(" ", "").lower()

# clear_screen()

# messages: list[dict] = []

# user_prompt: str = (
#     "If it takes one hour for a pair of pants to dry on the rooftop, how long will it take for ten pairs of pants to dry on the rooftop?"
# )

# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(host=BASE_URL)

# start_time: float = time.perf_counter()

# response: ChatResponse = client.chat(
#     # NEW
#     # think=True,
#     think=False,  # Default: False
#     #
#     stream=False,
#     model=MODEL_NAME,
#     messages=messages,
#     options={"temperature": TEMPERATURE},
# )

# end_time: float = time.perf_counter()
# elapsed_time: float = end_time - start_time
# formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

# assistant_answer: Optional[str] = response.message.content

# if not assistant_answer:
#     assistant_answer = "[red][bold][-][/bold] No content received![/red]"

# # NEW
# assistant_thinking: Optional[str] = response.message.thinking

# # NEW
# if not assistant_thinking:
#     assistant_thinking = "No thinking received!"

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
# print(f"Elapsed Time: {formatted_elapsed_time}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
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
# **************************************************


# **************************************************
# Step (12)
# **************************************************
# - Without History
# - Simple Text Chat Bot
# - System Prompt AND System Message
# **************************************************
# import time

# from typing import Final
# from typing import Optional

# from ollama import Client
# from ollama import ChatResponse

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# from dt_utility import clear_screen
# from dt_utility import format_seconds

# TEMPERATURE: Final[float] = 0.7
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# # NEW
# # MODEL_NAME: str = "gemma3:1b".replace(" ", "").lower()
# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()

# # NEW
# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."
# SYSTEM_MESSAGE: Final[dict] = {"role": "system", "content": SYSTEM_PROMPT}

# clear_screen()

# # NEW
# while True:
#     print("=" * 50)
#     user_prompt: str = input("User: ").strip()

#     if user_prompt.lower() in ["bye", "exit", "quit"]:
#         print("[yellow]Goodbye![/yellow]")
#         print("=" * 50)
#         print()
#         break

#     messages: list[dict] = []  # Reset
#     messages.append(SYSTEM_MESSAGE)

#     user_message: dict = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     client = Client(host=BASE_URL)

#     start_time: float = time.perf_counter()

#     response: ChatResponse = client.chat(
#         think=False,
#         stream=False,
#         model=MODEL_NAME,
#         messages=messages,
#         options={"temperature": TEMPERATURE},
#     )

#     end_time: float = time.perf_counter()
#     elapsed_time: float = end_time - start_time
#     formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

#     assistant_answer: Optional[str] = response.message.content

#     if not assistant_answer:
#         assistant_answer = "[red][bold][-][/bold] No content received![/red]"

#     print("-" * 50)
#     console = Console()
#     markdown = Markdown(markup=assistant_answer)
#     console.print(markdown)
#     print("-" * 50)
#     print(f"Elapsed Time: {formatted_elapsed_time}")
#     print("=" * 50)
#     print()
# **************************************************


# **************************************************
# Step (13)
# **************************************************
# - With History
# - Simple Text Chat Bot
# **************************************************
# import time

# from typing import Final
# from typing import Optional

# from ollama import Client
# from ollama import ChatResponse

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# from dt_utility import clear_screen
# from dt_utility import format_seconds

# TEMPERATURE: Final[float] = 0.7
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# # MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()

# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."
# SYSTEM_MESSAGE: Final[dict] = {"role": "system", "content": SYSTEM_PROMPT}

# clear_screen()

# # NEW
# messages: list[dict] = []
# messages.append(SYSTEM_MESSAGE)

# while True:
#     print("=" * 50)
#     user_prompt: str = input("User: ").strip()

#     if user_prompt.lower() in ["bye", "exit", "quit"]:
#         print("[yellow]Goodbye![/yellow]")
#         print("=" * 50)
#         print()
#         break

#     # NEW
#     # messages: list[dict] = []
#     # messages.append(SYSTEM_MESSAGE)

#     user_message: dict = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     client = Client(host=BASE_URL)

#     start_time: float = time.perf_counter()

#     response: ChatResponse = client.chat(
#         think=False,
#         stream=False,
#         model=MODEL_NAME,
#         messages=messages,
#         options={"temperature": TEMPERATURE},
#     )

#     end_time: float = time.perf_counter()
#     elapsed_time: float = end_time - start_time
#     formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

#     # در این مثال، فرض بر این است که حتما جواب داریم
#     assistant_answer: Optional[str] = response.message.content

#     if not assistant_answer:
#         assistant_answer = "[red][bold][-][/bold] No content received![/red]"

#     # NEW
#     assistant_message: dict = {"role": "assistant", "content": assistant_answer}
#     messages.append(assistant_message)

#     print("-" * 50)
#     console = Console()
#     markdown = Markdown(markup=assistant_answer)
#     console.print(markdown)
#     print("-" * 50)
#     print(f"Elapsed Time: {formatted_elapsed_time}")
#     print("=" * 50)
#     print()
# **************************************************


# **************************************************
# Step (14) - Best Practice (1)
# **************************************************
# import time

# from typing import Final
# from typing import Optional

# from ollama import Client
# from ollama import ChatResponse

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# from dt_utility import clear_screen
# from dt_utility import format_seconds

# # NEW
# USER_QUESTION: Final[str] = "User: "
# EXIT_COMMANDS: Final[list[str]] = [
#     "bye".replace(" ", "").lower(),
#     "exit".replace(" ", "").lower(),
#     "quit".replace(" ", "").lower(),
# ]

# # NEW
# ROLE_USER: Final[str] = "user".replace(" ", "").lower()
# ROLE_SYSTEM: Final[str] = "system".replace(" ", "").lower()
# ROLE_ASSISTANT: Final[str] = "assistant".replace(" ", "").lower()

# # NEW
# KEY_NAME_ROLE: Final[str] = "role".replace(" ", "").lower()
# KEY_NAME_CONTENT: Final[str] = "content".replace(" ", "").lower()
# KEY_NAME_TEMPRETURE: Final[str] = "temperature".replace(" ", "").lower()

# TEMPERATURE: Final[float] = 0.7
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# # MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()

# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."

# # NEW
# SYSTEM_MESSAGE: Final[dict] = {
#     KEY_NAME_ROLE: ROLE_SYSTEM,
#     KEY_NAME_CONTENT: SYSTEM_PROMPT,
# }
# # SYSTEM_MESSAGE: Final[dict] = {"role": "system", "content": SYSTEM_PROMPT}

# clear_screen()

# messages: list[dict] = []
# messages.append(SYSTEM_MESSAGE)

# while True:
#     print("=" * 50)

#     # NEW
#     # user_prompt: str = input("User: ").strip()
#     user_prompt: str = input(USER_QUESTION).strip()

#     # NEW
#     # if user_prompt.lower() in ["bye", "exit", "quit"]:
#     if user_prompt.lower() in EXIT_COMMANDS:
#         print("[yellow]Goodbye![/yellow]")
#         print("=" * 50)
#         print()
#         break

#     # NEW
#     # user_message: dict = {"role": "user", "content": user_prompt}
#     user_message: dict = {
#         KEY_NAME_ROLE: ROLE_USER,
#         KEY_NAME_CONTENT: user_prompt,
#     }

#     messages.append(user_message)

#     client = Client(host=BASE_URL)

#     start_time: float = time.perf_counter()

#     response: ChatResponse = client.chat(
#         think=False,
#         stream=False,
#         model=MODEL_NAME,
#         messages=messages,
#         # NEW
#         # options={"temperature": TEMPERATURE},
#         options={KEY_NAME_TEMPRETURE: TEMPERATURE},
#     )

#     end_time: float = time.perf_counter()
#     elapsed_time: float = end_time - start_time
#     formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

#     # در این مثال، فرض بر این است که حتما جواب داریم
#     assistant_answer: Optional[str] = response.message.content

#     if not assistant_answer:
#         assistant_answer = "[red][bold][-][/bold] No content received![/red]"

#     # NEW
#     # assistant_message: dict = {"role": "assistant", "content": assistant_answer}
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
#     print(f"Elapsed Time: {formatted_elapsed_time}")
#     print("=" * 50)
#     print()
# **************************************************


# **************************************************
# Step (15) - Best Practice (2)
# **************************************************
# import time

# from typing import Final
# from typing import Optional

# from ollama import Client
# from ollama import ChatResponse

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# from dt_utility import clear_screen
# from dt_utility import format_seconds

# USER_QUESTION: Final[str] = "User: "

# EXIT_COMMANDS: Final[list[str]] = [
#     "bye".replace(" ", "").lower(),
#     "exit".replace(" ", "").lower(),
#     "quit".replace(" ", "").lower(),
# ]

# ROLE_USER: Final[str] = "user".replace(" ", "").lower()
# ROLE_SYSTEM: Final[str] = "system".replace(" ", "").lower()
# ROLE_ASSISTANT: Final[str] = "assistant".replace(" ", "").lower()

# KEY_NAME_ROLE: Final[str] = "role".replace(" ", "").lower()
# KEY_NAME_CONTENT: Final[str] = "content".replace(" ", "").lower()
# KEY_NAME_TEMPRETURE: Final[str] = "temperature".replace(" ", "").lower()

# # NEW
# MESSAGE_GOODBYE: str = "Goodbye"
# MESSAGE_NO_CONTENT_RECEIVED: str = "No content received!"

# TEMPERATURE: Final[float] = 0.7
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# # MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()

# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."

# SYSTEM_MESSAGE: Final[dict] = {
#     KEY_NAME_ROLE: ROLE_SYSTEM,
#     KEY_NAME_CONTENT: SYSTEM_PROMPT,
# }


# # NEW
# def display_error_message(message: str) -> None:
#     """Display an error message"""

#     # message = fix_text(text=message)
#     result: str = f"[red bold][-] {message}![/red bold]"
#     print(result)


# # NEW
# def display_warning_message(message: str) -> None:
#     """Display an warning message"""

#     # message = fix_text(text=message)
#     result: str = f"[yellow bold][!] {message}![/yellow bold]"
#     print(result)


# # NEW
# def chat(
#     messages: list[dict],
#     think: bool = False,
#     base_url: str = BASE_URL,
#     model_name: str = MODEL_NAME,
#     temperature: float = TEMPERATURE,
# ) -> Optional[str]:
#     """Chat with Ollama service."""

#     client = Client(host=base_url)

#     response: ChatResponse = client.chat(
#         think=think,
#         stream=False,
#         model=model_name,
#         messages=messages,
#         options={KEY_NAME_TEMPRETURE: temperature},
#     )

#     assistant_answer: Optional[str] = response.message.content

#     return assistant_answer


# def main() -> None:
#     """The main of program"""

#     clear_screen()

#     messages: list[dict] = []
#     messages.append(SYSTEM_MESSAGE)

#     while True:
#         print("=" * 50)
#         user_prompt: str = input(USER_QUESTION).strip()

#         if user_prompt.lower() in EXIT_COMMANDS:
#             # NEW
#             display_warning_message(message=MESSAGE_GOODBYE)
#             print("=" * 50)
#             break

#         user_message: dict = {
#             KEY_NAME_ROLE: ROLE_USER,
#             KEY_NAME_CONTENT: user_prompt,
#         }

#         messages.append(user_message)

#         start_time: float = time.perf_counter()

#         assistant_answer: Optional[str] = chat(
#             messages=messages,
#         )

#         end_time: float = time.perf_counter()
#         elapsed_time: float = end_time - start_time
#         formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

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
#         print(f"Elapsed Time: {formatted_elapsed_time}")
#         print("=" * 50)
#         print()


# # NEW
# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()
#         print("=" * 50)

#     except Exception as exception:
#         print()
#         display_error_message(message=str(exception))
#         print("=" * 50)

#     finally:
#         print()
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# messages:

# System Message
# User Message 1
# Assistant Message 1
# User Message 2
# Assistant Message 2
# User Message 3
#   Assistant Answer: None OR "" -> messages.pop()

# The 'messages' will be:

# System Message
# User Message 1
# Assistant Message 1
# User Message 2
# Assistant Message 2
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# Step (16) - Best Practice (3) - Calculate Input / Output Tokens
# **************************************************
# import time

# from typing import Final
# from typing import Optional

# from ollama import Client
# from ollama import ChatResponse

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# # NEW
# # from dt_utility import clear_screen, format_seconds
# # from dt_utility import clear_screen
# # from dt_utility import format_seconds
# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_error_message,
#     display_warning_message,
#     display_information_message,
# )

# USER_QUESTION: Final[str] = "User: "

# EXIT_COMMANDS: Final[list[str]] = [
#     "bye".replace(" ", "").lower(),
#     "exit".replace(" ", "").lower(),
#     "quit".replace(" ", "").lower(),
# ]

# ROLE_USER: Final[str] = "user".replace(" ", "").lower()
# ROLE_SYSTEM: Final[str] = "system".replace(" ", "").lower()
# ROLE_ASSISTANT: Final[str] = "assistant".replace(" ", "").lower()

# KEY_NAME_ROLE: Final[str] = "role".replace(" ", "").lower()
# KEY_NAME_CONTENT: Final[str] = "content".replace(" ", "").lower()
# KEY_NAME_TEMPRETURE: Final[str] = "temperature".replace(" ", "").lower()

# MESSAGE_GOODBYE: Final[str] = "Goodbye"
# MESSAGE_NO_CONTENT_RECEIVED: Final[str] = "No content received!"

# TEMPERATURE: Final[float] = 0.7
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# # MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()

# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."

# SYSTEM_MESSAGE: Final[dict] = {
#     KEY_NAME_ROLE: ROLE_SYSTEM,
#     KEY_NAME_CONTENT: SYSTEM_PROMPT,
# }


# def chat(
#     messages: list[dict],
#     think: bool = False,
#     # NEW
#     notify: bool = False,
#     #
#     base_url: str = BASE_URL,
#     model_name: str = MODEL_NAME,
#     temperature: float = TEMPERATURE,
#     # NEW
#     # ) -> Optional[str]:
# ) -> tuple[Optional[str], int, int]:
#     """Chat with Ollama service."""

#     client = Client(host=base_url)

#     # NEW
#     if notify:
#         display_information_message(message=f"Ollama '{model_name}' chat started...")

#     response: ChatResponse = client.chat(
#         think=think,
#         stream=False,
#         model=model_name,
#         messages=messages,
#         options={KEY_NAME_TEMPRETURE: temperature},
#     )

#     # NEW
#     if notify:
#         display_information_message(message=f"Ollama '{model_name}' chat finished.")

#     assistant_answer: Optional[str] = response.message.content

#     # NEW
#     prompt_tokens: int = 0
#     completion_tokens: int = 0

#     # NEW
#     # شرط ذیل، برای حلال و حرام است
#     if assistant_answer:
#         if response.eval_count:
#             completion_tokens = response.eval_count
#         if response.prompt_eval_count:
#             prompt_tokens = response.prompt_eval_count

#     # NEW
#     return assistant_answer, prompt_tokens, completion_tokens
#     # return (assistant_answer, prompt_tokens, completion_tokens)


# def main() -> None:
#     """The main of program"""

#     clear_screen()

#     messages: list[dict] = []
#     messages.append(SYSTEM_MESSAGE)

#     while True:
#         print("=" * 50)
#         user_prompt: str = input(USER_QUESTION).strip()

#         if user_prompt.lower() in EXIT_COMMANDS:
#             display_warning_message(message=MESSAGE_GOODBYE)
#             print("=" * 50)
#             break

#         user_message: dict = {
#             KEY_NAME_ROLE: ROLE_USER,
#             KEY_NAME_CONTENT: user_prompt,
#         }

#         messages.append(user_message)

#         start_time: float = time.perf_counter()

#         # NEW
#         # assistant_answer, _, _ = chat(
#         #     messages=messages,
#         # )

#         # NEW
#         assistant_answer, prompt_tokens, completion_tokens = chat(
#             # NEW
#             notify=True,
#             #
#             messages=messages,
#         )

#         end_time: float = time.perf_counter()
#         elapsed_time: float = end_time - start_time
#         formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

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
#         print(f"Elapsed Time: {formatted_elapsed_time}")
#         # NEW
#         print("-" * 50)
#         print(f"Prompt Tokens (Input): {prompt_tokens}")
#         print("-" * 50)
#         print(f"Completion Tokens (Output): {completion_tokens}")
#         #
#         print("=" * 50)
#         print()


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()
#         print("=" * 50)

#     except Exception as exception:
#         print()
#         display_error_message(message=str(exception))
#         print("=" * 50)

#     finally:
#         print()
# **************************************************


# **************************************************
# Step (17) - Best Practice (4)
# **************************************************
# import time
# import dt_ollama as ollama
# import dt_llm_utility as llm_utility

# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_error_message,
#     display_warning_message,
# )

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown


# def main() -> None:
#     """The main of program"""

#     clear_screen()

#     messages: list[dict] = []
#     messages.append(llm_utility.SYSTEM_MESSAGE)

#     while True:
#         print("=" * 50)
#         user_prompt: str = input(llm_utility.USER_QUESTION).strip()

#         if user_prompt.lower() in llm_utility.EXIT_COMMANDS:
#             display_warning_message(message=llm_utility.MESSAGE_GOODBYE)
#             print("=" * 50)
#             break

#         user_message: dict = {
#             llm_utility.KEY_NAME_ROLE: llm_utility.ROLE_USER,
#             llm_utility.KEY_NAME_CONTENT: user_prompt,
#         }

#         messages.append(user_message)

#         start_time: float = time.perf_counter()

#         assistant_answer, prompt_tokens, completion_tokens = ollama.chat(
#             notify=True,
#             messages=messages,
#         )

#         end_time: float = time.perf_counter()
#         elapsed_time: float = end_time - start_time
#         formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

#         # if not assistant_answer:
#         #     messages.pop()
#         #     assistant_answer = llm_utility.MESSAGE_NO_CONTENT_RECEIVED
#         # else:
#         #     assistant_message: dict = {
#         #         llm_utility.KEY_NAME_ROLE: llm_utility.ROLE_ASSISTANT,
#         #         llm_utility.KEY_NAME_CONTENT: assistant_answer,
#         #     }

#         #     messages.append(assistant_message)

#         # با تشکر از امیرحسین مرجانی
#         if assistant_answer:
#             assistant_message: dict = {
#                 llm_utility.KEY_NAME_ROLE: llm_utility.ROLE_ASSISTANT,
#                 llm_utility.KEY_NAME_CONTENT: assistant_answer,
#             }

#             messages.append(assistant_message)
#         else:
#             messages.pop()
#             assistant_answer = llm_utility.MESSAGE_NO_CONTENT_RECEIVED

#         print("-" * 50)
#         console = Console()
#         markdown = Markdown(markup=assistant_answer)
#         console.print(markdown)
#         print("-" * 50)
#         print(f"Elapsed Time: {formatted_elapsed_time}")
#         print("-" * 50)
#         print(f"Prompt Tokens (Input): {prompt_tokens}")
#         print("-" * 50)
#         print(f"Completion Tokens (Output): {completion_tokens}")
#         print("=" * 50)
#         print()


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()
#         print("=" * 50)

#     except Exception as exception:
#         print()
#         display_error_message(message=str(exception))
#         print("=" * 50)

#     finally:
#         print()
# **************************************************
