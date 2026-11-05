"""
Update all downloaded models using the ollama API.
"""

import ollama

from rich import print
from ollama import ListResponse

from dt_utility import (
    clear_screen,
    display_divider,
    display_main_divider,
    display_title_message,
)

clear_screen()
display_main_divider(count=70)

ollama_list: ListResponse = ollama.list()
models = ollama_list.models

model_names: list[str] = []
for model_item in models:
    if model_item.model:
        model_names.append(model_item.model)
model_names.sort()

message: str = f"Updating all downloaded models (Model Count: {len(model_names)})"
display_title_message(message=message)
display_divider(count=70)

for index, model_name in enumerate(model_names, start=1):
    if model_name.startswith("hf.co/"):
        continue  # Skip Hugging Face models

    item: str = f"{index:>2} Updating Model: [green bold]{model_name:.<51}[/green bold]"
    print(item)
    ollama.pull(model=model_name)

display_main_divider(count=70)
print()
