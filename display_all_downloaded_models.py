"""
Display all downloaded models using the Ollama API (Service).
"""

# **************************************************
import os
import ollama
from rich import print
from ollama import ListResponse

os.system(command="cls" if os.name == "nt" else "clear")

ollama_list: ListResponse = ollama.list()

print(ollama_list)

# Bad Practice
# print(ollama_list["models"])

# Best Practice
# print(ollama_list.models)
# **************************************************


# **************************************************
# import os
# import ollama
# from rich import print
# from ollama import ListResponse

# os.system(command="cls" if os.name == "nt" else "clear")

# ollama_list: ListResponse = ollama.list()
# models = ollama_list.models

# for model_item in models:
#     print(model_item)
#     print("-" * 50)

#     # print(model_item.model)

#     # if not model_item.details:
#     #     print(f"[-] {model_item.model}")
#     # else:
#     #     print(f"{model_item.model} - {model_item.details.parameter_size}")
# **************************************************


# **************************************************
# import os
# import ollama
# from rich import print
# from ollama import ListResponse

# os.system(command="cls" if os.name == "nt" else "clear")

# ollama_list: ListResponse = ollama.list()
# models = ollama_list.models

# model_names: list[str] = []
# for model_item in models:
#     if model_item.model:
#         model_names.append(model_item.model)

# model_names.sort()

# for model_name in model_names:
#     print(model_name)

# # for index, model_name in enumerate(model_names):
# #     print(index + 1, model_name)

# # for index, model_name in enumerate(model_names, start=1):
# #     print(index, model_name)

# # for index, model_name in enumerate(model_names, start=1):
# #     index_string: str = str(index).rjust(2, " ")
# #     print(index_string, model_name)

# print()
# **************************************************
