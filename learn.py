# **************************************************
import ollama

from rich import print

from dt_utility import (
    clear_screen,
    display_main_divider,
)

clear_screen()
display_main_divider()

# همان‌طور که قبلا گفتم، دستور ذیل، همیشه کار نمی‌کند
# print(f"Version of 'ollama' package: {ollama.__version__}")

display_main_divider()
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
# Learning 'generate()' method
# **************************************************
# ConnectionError: Failed to connect to Ollama.
# Please check that Ollama is downloaded, running and
# accessible. https://ollama.com/download
#
# > ollama start
# > ollama serve
# **************************************************
# import ollama

# from rich import print

# from dt_utility import (
#     clear_screen,
#     display_divider,
#     display_main_divider,
# )

# clear_screen()
# display_main_divider()

# generate_completion = ollama.generate(
#     model="gemma3:1b",
#     prompt="Tell me a joke.",
# )

# print(generate_completion)
# display_divider()
# print(generate_completion.response)

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Learning 'chat()' method
# **************************************************
# import ollama

# from rich import print

# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )

# clear_screen()
# display_main_divider()

# # NEW: 'generate()' -> 'chat()'
# response = ollama.chat(
#     model="gemma3:1b",
#     # NEW
#     messages=[{"role": "user", "content": "Tell me a joke."}],
# )

# print(response)

# display_main_divider()
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
# import ollama

# from typing import (
#     Dict,
#     List,
#     Final,
# )

# from rich import print

# from dt_utility import (
#     clear_screen,
#     display_divider,
#     display_main_divider,
# )

# # NEW: Type Hint: لوس بازی
# from ollama import ChatResponse

# # NEW
# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()

# clear_screen()
# display_main_divider()

# # NEW
# messages: List[Dict] = []
# # messages: list[dict] = []

# # NEW
# user_prompt: str = "Tell me a joke."
# user_message: Dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# # NEW: ChatResponse
# response: ChatResponse = ollama.chat(
#     model=MODEL_NAME,
#     messages=messages,
# )

# # NEW
# print(response["message"]["content"])

# display_divider()
# # NEW:‌ ‌Best Practice
# print(response.message.content)

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Learning Client
# **************************************************
# from typing import (
#     Dict,
#     List,
#     Final,
# )

# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )

# from rich import print
# from ollama import ChatResponse

# # NEW
# # import ollama
# from ollama import Client

# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()

# # NEW
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()
# # BASE_URL: Final[str] = "http://localhost:11434".replace(" ", "").lower()

# clear_screen()
# display_main_divider()

# messages: List[Dict] = []

# # NEW: Change 'user_prompt' value
# user_prompt: str = "Tell me a short science fiction story."

# user_message: Dict = {"role": "user", "content": user_prompt}
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

# print(response.message.content)

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Learning 'rich': Markdown
# **************************************************
# from typing import (
#     Dict,
#     List,
#     Final,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from rich import print

# from dt_utility import (
#     clear_screen,
#     display_divider,
#     display_main_divider,
# )

# # NEW
# from typing import Optional
# from rich.console import Console
# from rich.markdown import Markdown

# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# clear_screen()
# display_main_divider()

# messages: List[Dict] = []

# # NEW: Change 'user_prompt' value
# user_prompt: str = "Write a python code to print numbers between one to ten."

# user_message: Dict = {"role": "user", "content": user_prompt}
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

# # NEW: assistant_answer is None or "" (Null String)
# if not assistant_answer:
#     assistant_answer = "[red][bold][-][/bold] No content received![/red]"

# # NEW
# print(assistant_answer)

# # NEW
# console = Console()
# markdown = Markdown(markup=assistant_answer)
# display_divider()
# console.print(markdown)

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Learning Temperature
# **************************************************
# from typing import (
#     Dict,
#     List,
#     Final,
#     Optional,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# # NEW
# TEMPERATURE: Final[float] = 0.8

# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# clear_screen()
# display_main_divider()

# messages: List[Dict] = []

# # NEW: Change 'user_prompt' value
# user_prompt: str = "Tell me a long science fiction story."

# user_message: Dict = {"role": "user", "content": user_prompt}
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

# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Learning Stream
# **************************************************
# from typing import (
#     Dict,
#     List,
#     Final,
#     Optional,
#     # NEW
#     Iterator,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from rich import print

# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )

# TEMPERATURE: Final[float] = 0.8
# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# clear_screen()
# display_main_divider()

# messages: List[Dict] = []

# user_prompt: str = "Tell me a long science fiction story."
# user_message: Dict = {"role": "user", "content": user_prompt}
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

# # NEW
# for chunk in response_stream:
#     content: Optional[str] = chunk.message.content
#     if content:
#         # print(content)
#         print(content, end="", flush=True)

# # NEW
# print()

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Learning Elapsed Time
# **************************************************
# # NEW
# import time

# from typing import (
#     Dict,
#     List,
#     Final,
#     Optional,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from dt_utility import (
#     clear_screen,
#     display_divider,
#     display_main_divider,
# )

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# TEMPERATURE: Final[float] = 0.8
# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# clear_screen()
# display_main_divider()

# messages: List[Dict] = []

# # NEW: Change 'user_prompt' value
# user_prompt: str = "Tell me a joke."

# user_message: Dict = {"role": "user", "content": user_prompt}
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

# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)

# # NEW
# display_divider()
# print(f"Elapsed Time: {elapsed_time:.2f} second(s).")

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Learning Elapsed Time with 'perf_counter()'
# **************************************************
# import time

# from typing import (
#     Dict,
#     List,
#     Final,
#     Optional,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from dt_utility import (
#     clear_screen,
#     display_divider,
#     display_main_divider,
#     # NEW
#     format_seconds,
# )

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# TEMPERATURE: Final[float] = 0.8
# MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# clear_screen()
# display_main_divider()

# messages: List[Dict] = []

# user_prompt: str = "Tell me a joke."
# user_message: Dict = {"role": "user", "content": user_prompt}
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
# end_time: float = time.perf_counter()
# elapsed_time: float = end_time - start_time
# formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

# assistant_answer: Optional[str] = response.message.content

# if not assistant_answer:
#     assistant_answer = "[red][bold][-][/bold] No content received![/red]"

# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)

# display_divider()
# # NEW
# # print(f"Elapsed Time: {elapsed_time:.2f} second(s).")
# print(f"Elapsed Time: {formatted_elapsed_time}")

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Learning Reasoning / Thinking
# **************************************************
# import time

# from typing import (
#     Dict,
#     List,
#     Final,
#     Optional,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_divider,
#     display_main_divider,
# )

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# TEMPERATURE: Final[float] = 0.8
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# # NEW
# MODEL_NAME: Final[str] = "deepseek-r1:1.5b".replace(" ", "").lower()

# clear_screen()
# display_main_divider()

# messages: List[Dict] = []

# # NEW: Change 'user_prompt' value
# user_prompt: str = "If it takes one hour for a pair of pants to dry on the rooftop, how long will it take for ten pairs of pants to dry on the rooftop?"

# user_message: Dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# client = Client(host=BASE_URL)

# start_time: float = time.perf_counter()

# response: ChatResponse = client.chat(
#     # NEW
#     # think=True,
#     # think=None,  # Default: False
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
#     assistant_answer = "[red][bold][-][/bold] No thinking received![/red]"

# print(response)

# display_divider()
# if assistant_thinking:
#     # NEW
#     console = Console()
#     markdown = Markdown(markup=assistant_thinking)
#     console.print(markdown)
#     display_divider()

# console = Console()
# markdown = Markdown(markup=assistant_answer)
# console.print(markdown)

# display_divider()
# print(f"Elapsed Time: {formatted_elapsed_time}")

# display_main_divider()
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
# - Simple Text Chatbot
# - Without History (Memory)
# - System Prompt AND System Message
# **************************************************
# import time

# from typing import (
#     Dict,
#     List,
#     Final,
#     Optional,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_divider,
#     display_main_divider,
#     display_tiny_divider,
#     display_title_message,
#     display_warning_message,
# )

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# VERSION: Final[str] = "0.1.0"

# TEMPERATURE: Final[float] = 0.8
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# # NEW
# # MODEL_NAME: str = "gemma3:1b".replace(" ", "").lower()
# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()

# # NEW
# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."
# SYSTEM_MESSAGE: Final[Dict] = {"role": "system", "content": SYSTEM_PROMPT}

# clear_screen()
# display_main_divider()

# title: str = f"Dariush Tasdighi - Simple Chatbot ({VERSION})"
# display_title_message(message=title)

# # NEW
# while True:
#     display_divider()
#     user_prompt: str = input("User: ").strip()

#     if not user_prompt:
#         continue

#     if user_prompt.lower() in ["bye", "exit", "quit"]:
#         message: str = "Goodbye!"
#         display_divider()
#         display_warning_message(message=message)
#         display_main_divider()
#         print()
#         break

#     messages: List[Dict] = []  # Reset
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

#     display_tiny_divider()
#     console = Console()
#     markdown = Markdown(markup=assistant_answer)
#     console.print(markdown)

#     display_tiny_divider()
#     print(f"Elapsed Time: {formatted_elapsed_time}")

#     display_divider()
#     print()
# **************************************************


# **************************************************
# - With History (Memory)
# - Simple Text Chat Bot
# **************************************************
# import time

# from typing import (
#     Dict,
#     List,
#     Final,
#     Optional,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_divider,
#     display_main_divider,
#     display_tiny_divider,
#     display_title_message,
#     display_warning_message,
# )

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# VERSION: Final[str] = "0.1.0"

# TEMPERATURE: Final[float] = 0.8
# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."
# SYSTEM_MESSAGE: Final[Dict] = {"role": "system", "content": SYSTEM_PROMPT}

# clear_screen()
# display_main_divider()

# title: str = f"Dariush Tasdighi - Simple Chatbot ({VERSION})"
# display_title_message(message=title)

# # NEW
# messages: List[Dict] = []
# messages.append(SYSTEM_MESSAGE)

# while True:
#     display_divider()
#     user_prompt: str = input("User: ").strip()

#     if not user_prompt:
#         continue

#     if user_prompt.lower() in ["bye", "exit", "quit"]:
#         message: str = "Goodbye!"
#         display_divider()
#         display_warning_message(message=message)
#         display_main_divider()
#         print()
#         break

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
#         # NEW
#         messages.pop()

#         assistant_answer = "[red][bold][-][/bold] No content received![/red]"
#     else:
#         # NEW
#         assistant_message: Dict = {"role": "assistant", "content": assistant_answer}
#         messages.append(assistant_message)

#     display_tiny_divider()
#     console = Console()
#     markdown = Markdown(markup=assistant_answer)
#     console.print(markdown)

#     display_tiny_divider()
#     print(f"Elapsed Time: {formatted_elapsed_time}")

#     display_divider()
#     print()
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
# import time

# from typing import (
#     Dict,
#     List,
#     Final,
#     Optional,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_divider,
#     display_main_divider,
#     display_tiny_divider,
#     display_title_message,
#     display_warning_message,
# )

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# VERSION: Final[str] = "0.1.0"
# TITLE: Final[str] = f"Dariush Tasdighi - Simple Chatbot ({VERSION})"

# TEMPERATURE: Final[float] = 0.8
# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# MESSAGE_GOODBYE: Final[str] = "Goodbye"
# MESSAGE_NO_CONTENT_RECEIVED: Final[str] = "No content received!"

# # NEW
# USER_PROMPT: Final[str] = "User: "
# EXIT_COMMANDS: Final[List[str]] = [
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

# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."

# SYSTEM_MESSAGE: Final[dict] = {
#     KEY_NAME_ROLE: ROLE_SYSTEM,
#     KEY_NAME_CONTENT: SYSTEM_PROMPT,
# }
# # SYSTEM_MESSAGE: Final[dict] = {"role": "system", "content": SYSTEM_PROMPT}

# clear_screen()
# display_main_divider()

# display_title_message(message=TITLE)

# messages: List[Dict] = []
# messages.append(SYSTEM_MESSAGE)

# while True:
#     display_divider()
#     user_prompt: str = input(USER_PROMPT).strip()

#     if not user_prompt:
#         continue

#     if user_prompt.lower() in EXIT_COMMANDS:
#         display_divider()
#         display_warning_message(message=MESSAGE_GOODBYE)
#         display_main_divider()
#         print()
#         break

#     user_message: Dict = {
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
#         options={KEY_NAME_TEMPRETURE: TEMPERATURE},
#     )

#     end_time: float = time.perf_counter()
#     elapsed_time: float = end_time - start_time
#     formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

#     assistant_answer: Optional[str] = response.message.content

#     if not assistant_answer:
#         messages.pop()
#         assistant_answer = f"[red][bold][-][/bold] {MESSAGE_NO_CONTENT_RECEIVED}![/red]"
#     else:
#         assistant_message: Dict = {
#             KEY_NAME_ROLE: ROLE_ASSISTANT,
#             KEY_NAME_CONTENT: assistant_answer,
#         }

#         messages.append(assistant_message)

#     display_tiny_divider()
#     console = Console()
#     markdown = Markdown(markup=assistant_answer)
#     console.print(markdown)

#     display_tiny_divider()
#     print(f"Elapsed Time: {formatted_elapsed_time}")

#     display_divider()
#     print()
# **************************************************


# **************************************************
# import time

# from typing import (
#     Dict,
#     List,
#     Final,
#     Tuple,
#     Optional,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_divider,
#     display_main_divider,
#     display_tiny_divider,
#     display_title_message,
#     display_warning_message,
# )

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# VERSION: Final[str] = "0.1.0"
# TITLE: Final[str] = f"Dariush Tasdighi - Simple Chatbot ({VERSION})"

# MODEL_TEMPERATURE: Final[float] = 0.8
# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# MESSAGE_GOODBYE: Final[str] = "Goodbye"
# MESSAGE_NO_CONTENT_RECEIVED: Final[str] = "No content received!"

# USER_PROMPT: Final[str] = "User: "
# EXIT_COMMANDS: Final[List[str]] = [
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

# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."

# SYSTEM_MESSAGE: Final[dict] = {
#     KEY_NAME_ROLE: ROLE_SYSTEM,
#     KEY_NAME_CONTENT: SYSTEM_PROMPT,
# }


# def chat(
#     messages: List[Dict],
#     think: bool = False,
#     base_url: str = BASE_URL,
#     model_name: str = MODEL_NAME,
#     temperature: float = MODEL_TEMPERATURE,
# ) -> Tuple[Optional[str], float, int, int]:
#     """Chat with Ollama service."""

#     client = Client(host=base_url)

#     start_time: float = time.perf_counter()

#     response: ChatResponse = client.chat(
#         think=think,
#         stream=False,
#         model=model_name,
#         messages=messages,
#         options={KEY_NAME_TEMPRETURE: temperature},
#     )

#     end_time: float = time.perf_counter()
#     elapsed_time: float = end_time - start_time

#     assistant_answer: Optional[str] = response.message.content

#     prompt_tokens: int = 0  # Input Tokens
#     completion_tokens: int = 0  # Output Tokens

#     # برای حلال شدن سامانه
#     if assistant_answer:
#         if response.eval_count is not None:
#             completion_tokens = response.eval_count
#         if response.prompt_eval_count is not None:
#             prompt_tokens = response.prompt_eval_count

#     return assistant_answer, elapsed_time, prompt_tokens, completion_tokens


# clear_screen()
# display_main_divider()

# display_title_message(message=TITLE)

# messages: List[Dict] = []
# messages.append(SYSTEM_MESSAGE)

# while True:
#     display_divider()
#     user_prompt: str = input(USER_PROMPT).strip()

#     if not user_prompt:
#         continue

#     if user_prompt.lower() in EXIT_COMMANDS:
#         display_divider()
#         display_warning_message(message=MESSAGE_GOODBYE)
#         display_main_divider()
#         print()
#         break

#     user_message: Dict = {
#         KEY_NAME_ROLE: ROLE_USER,
#         KEY_NAME_CONTENT: user_prompt,
#     }

#     messages.append(user_message)

#     # assistant_answer, elapsed_time, _, _ = chat(
#     #     messages=messages,
#     # )

#     assistant_answer, elapsed_time, prompt_tokens, completion_tokens = chat(
#         messages=messages,
#     )

#     formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

#     if not assistant_answer:
#         messages.pop()
#         assistant_answer = f"[red][bold][-][/bold] {MESSAGE_NO_CONTENT_RECEIVED}![/red]"
#     else:
#         assistant_message: Dict = {
#             KEY_NAME_ROLE: ROLE_ASSISTANT,
#             KEY_NAME_CONTENT: assistant_answer,
#         }

#         messages.append(assistant_message)

#     display_tiny_divider()
#     console = Console()
#     markdown = Markdown(markup=assistant_answer)
#     console.print(markdown)

#     display_tiny_divider()
#     print(f"Elapsed Time..............: {formatted_elapsed_time}")

#     display_tiny_divider()
#     print(f"Prompt (Input) Tokens.....: {prompt_tokens}")

#     display_tiny_divider()
#     print(f"Completion (Output) Tokens: {completion_tokens}")

#     display_divider()
#     print()
# **************************************************


# **************************************************
# import time

# from typing import (
#     Dict,
#     List,
#     Final,
#     Tuple,
#     Optional,
# )

# from ollama import (
#     Client,
#     ChatResponse,
# )

# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_divider,
#     display_main_divider,
#     display_tiny_divider,
#     display_error_message,
#     display_title_message,
#     display_warning_message,
# )

# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

# VERSION: Final[str] = "0.1.0"
# TITLE: Final[str] = f"Dariush Tasdighi - Simple Chatbot ({VERSION})"

# MODEL_TEMPERATURE: Final[float] = 0.8
# MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()
# BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

# MESSAGE_GOODBYE: Final[str] = "Goodbye"
# MESSAGE_NO_CONTENT_RECEIVED: Final[str] = "No content received!"

# USER_PROMPT: Final[str] = "User: "
# EXIT_COMMANDS: Final[List[str]] = [
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

# SYSTEM_PROMPT: Final[str] = "You are a helpful AI assistant."

# SYSTEM_MESSAGE: Final[dict] = {
#     KEY_NAME_ROLE: ROLE_SYSTEM,
#     KEY_NAME_CONTENT: SYSTEM_PROMPT,
# }


# def chat(
#     messages: List[Dict],
#     think: bool = False,
#     base_url: str = BASE_URL,
#     model_name: str = MODEL_NAME,
#     temperature: float = MODEL_TEMPERATURE,
# ) -> Tuple[Optional[str], float, int, int]:
#     """Chat with Ollama service."""

#     client = Client(host=base_url)

#     start_time: float = time.perf_counter()

#     response: ChatResponse = client.chat(
#         think=think,
#         stream=False,
#         model=model_name,
#         messages=messages,
#         options={KEY_NAME_TEMPRETURE: temperature},
#     )

#     end_time: float = time.perf_counter()
#     elapsed_time: float = end_time - start_time

#     assistant_answer: Optional[str] = response.message.content

#     prompt_tokens: int = 0  # Input Tokens
#     completion_tokens: int = 0  # Output Tokens

#     # برای حلال شدن سامانه
#     if assistant_answer:
#         if response.eval_count is not None:
#             completion_tokens = response.eval_count
#         if response.prompt_eval_count is not None:
#             prompt_tokens = response.prompt_eval_count

#     return assistant_answer, elapsed_time, prompt_tokens, completion_tokens


# def main() -> None:
#     """Main function"""

#     clear_screen()
#     display_main_divider()

#     display_title_message(message=TITLE)

#     messages: List[Dict] = []
#     messages.append(SYSTEM_MESSAGE)

#     while True:
#         display_divider()
#         user_prompt: str = input(USER_PROMPT).strip()

#         if not user_prompt:
#             continue

#         if user_prompt.lower() in EXIT_COMMANDS:
#             display_divider()
#             display_warning_message(message=MESSAGE_GOODBYE)
#             return

#         user_message: Dict = {
#             KEY_NAME_ROLE: ROLE_USER,
#             KEY_NAME_CONTENT: user_prompt,
#         }

#         messages.append(user_message)

#         assistant_answer, elapsed_time, prompt_tokens, completion_tokens = chat(
#             messages=messages,
#         )

#         formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

#         if not assistant_answer:
#             messages.pop()
#             assistant_answer = f"[red][bold][-][/bold] {MESSAGE_NO_CONTENT_RECEIVED}![/red]"
#         else:
#             assistant_message: Dict = {
#                 KEY_NAME_ROLE: ROLE_ASSISTANT,
#                 KEY_NAME_CONTENT: assistant_answer,
#             }

#             messages.append(assistant_message)

#         display_tiny_divider()
#         console = Console()
#         markdown = Markdown(markup=assistant_answer)
#         console.print(markdown)

#         display_tiny_divider()
#         print(f"Elapsed Time..............: {formatted_elapsed_time}")

#         display_tiny_divider()
#         print(f"Prompt (Input) Tokens.....: {prompt_tokens}")

#         display_tiny_divider()
#         print(f"Completion (Output) Tokens: {completion_tokens}")

#         display_divider()
#         print()


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_divider()
#         display_error_message(message=str(exception))

#     finally:
#         display_main_divider()
#         print()
# **************************************************


# **************************************************
# from typing import (
#     Dict,
#     List,
#     Final,
# )

# from dt_utility import (
#     clear_screen,
#     format_seconds,
#     display_divider,
#     display_main_divider,
#     display_tiny_divider,
#     display_error_message,
#     display_title_message,
#     display_warning_message,
# )

# from dt_lm import (
#     ROLE_USER,
#     USER_PROMPT,
#     EXIT_COMMANDS,
#     KEY_NAME_ROLE,
#     ROLE_ASSISTANT,
#     SYSTEM_MESSAGE,
#     MESSAGE_GOODBYE,
#     KEY_NAME_CONTENT,
#     MESSAGE_NO_CONTENT_RECEIVED,
# )

# from rich import print
# from dt_ollama import chat
# from rich.console import Console
# from rich.markdown import Markdown

# VERSION: Final[str] = "0.1.0"
# TITLE: Final[str] = f"Dariush Tasdighi - Simple Chatbot ({VERSION})"


# def main() -> None:
#     """Main function"""

#     clear_screen()
#     display_main_divider()

#     display_title_message(message=TITLE)

#     messages: List[Dict] = []
#     messages.append(SYSTEM_MESSAGE)

#     while True:
#         display_divider()
#         user_prompt: str = input(USER_PROMPT).strip()

#         if not user_prompt:
#             continue

#         if user_prompt.lower() in EXIT_COMMANDS:
#             display_divider()
#             display_warning_message(message=MESSAGE_GOODBYE)
#             return

#         user_message: Dict = {
#             KEY_NAME_ROLE: ROLE_USER,
#             KEY_NAME_CONTENT: user_prompt,
#         }

#         messages.append(user_message)

#         assistant_answer, elapsed_time, prompt_tokens, completion_tokens = chat(
#             messages=messages,
#         )

#         formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

#         if not assistant_answer:
#             messages.pop()
#             assistant_answer = f"[red][bold][-][/bold] {MESSAGE_NO_CONTENT_RECEIVED}![/red]"
#         else:
#             assistant_message: Dict = {
#                 KEY_NAME_ROLE: ROLE_ASSISTANT,
#                 KEY_NAME_CONTENT: assistant_answer,
#             }

#             messages.append(assistant_message)

#         display_tiny_divider()
#         console = Console()
#         markdown = Markdown(markup=assistant_answer)
#         console.print(markdown)

#         display_tiny_divider()
#         print(f"Elapsed Time..............: {formatted_elapsed_time}")

#         display_tiny_divider()
#         print(f"Prompt (Input) Tokens.....: {prompt_tokens}")

#         display_tiny_divider()
#         print(f"Completion (Output) Tokens: {completion_tokens}")

#         display_divider()
#         print()


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_divider()
#         display_error_message(message=str(exception))

#     finally:
#         display_main_divider()
#         print()
# **************************************************
