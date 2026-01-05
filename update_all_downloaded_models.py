"""
Update all downloaded models using the ollama API.
"""

import os
import ollama
from rich import print
from ollama import ListResponse

os.system(command="cls" if os.name == "nt" else "clear")

ollama_list: ListResponse = ollama.list()
models = ollama_list.models

model_names: list[str] = []

for model_item in models:
    if model_item.model:
        model_names.append(model_item.model)

model_names.sort()

for index, model_name in enumerate(model_names, start=1):
    index_string: str = str(index).rjust(2, " ")
    print(index_string, "Updating... ", model_name)
    ollama.pull(model=model_name)

print()
