"""
Update all downloaded models using the ollama API.
"""

import ollama

from rich import print
from ollama import ListResponse
from dt_utility import clear_screen

clear_screen()
print("=" * 50)

ollama_list: ListResponse = ollama.list()
models = ollama_list.models

model_names: list[str] = []
for model_item in models:
    if model_item.model:
        model_names.append(model_item.model)
model_names.sort()

for index, model_name in enumerate(model_names, start=1):
    item: str = f"{index:>2} Updating Model: '{model_name}'..."
    print(item)
    ollama.pull(model=model_name)

print("=" * 50)
print()
