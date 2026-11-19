"""Dariush Tasdighi - Update Ollama Models"""

import ollama

from typing import (
    List,
    Final,
)

from dt_utility import (
    clear_screen,
    display_divider,
    display_main_divider,
    display_title_message,
)

from rich import print
from ollama import ListResponse

VERSION: Final[str] = "1.0.0"

clear_screen()
display_main_divider()

ollama_list: ListResponse = ollama.list()
models = ollama_list.models

model_names: List[str] = []
for model_item in models:
    if model_item.model:
        model_names.append(model_item.model)

model_names.sort()

message: str

message = f"Dariush Tasdighi - Update Ollama Models ({VERSION})"
display_title_message(message=message)
display_divider()

for index, model_name in enumerate(iterable=model_names, start=1):
    if model_name.startswith("hf.co/"):
        continue  # Skip Hugging Face models

    message = f"{index:>2} Updating [green bold]{model_name:.<38}[/green bold]"
    print(message)

    ollama.pull(model=model_name)

display_main_divider()
print()
