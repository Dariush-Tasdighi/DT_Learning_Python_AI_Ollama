"""
Display all downloaded models using the Ollama service.
"""

# **************************************************
# import ollama

# from rich import print

# # لوس‌بازی
# from ollama import ListResponse
# from dt_utility import clear_screen

# clear_screen()

# ollama_list: ListResponse = ollama.list()

# print(ollama_list)

# # - Bad Practice
# # print(ollama_list["models"])

# # - Best Practice
# # print(ollama_list.models)
# **************************************************


# **************************************************
# import ollama

# from dt_utility import (
#     clear_screen,
#     display_divider,
#     display_main_divider,
# )

# from rich import print
# from ollama import ListResponse

# clear_screen()
# display_main_divider()

# ollama_list: ListResponse = ollama.list()
# models = ollama_list.models

# for model_item in models:
#     print(model_item)
#     display_divider()

#     # print(model_item.model)

#     # print(f"{model_item.model} - {model_item.details.parameter_size}")

#     # if model_item.details is None:
#     #     print(f"[-] {model_item.model}")
#     # else:
#     #     print(f"{model_item.model} - {model_item.details.parameter_size}")

# display_main_divider()
# print()
# **************************************************


# **************************************************
# import ollama

# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )

# from rich import print
# from ollama import ListResponse

# clear_screen()
# display_main_divider()

# ollama_list: ListResponse = ollama.list()
# models = ollama_list.models

# model_names: list[str] = []
# for model_item in models:
#     if model_item.model is not None:
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
# #     # index_string: str = str(index).ljust(2, " ")
# #     print(index_string, model_name)

# # for index, model_name in enumerate(model_names, start=1):
# #     item: str = f"{index:<2} {model_name}"
# #     # item: str = f"{index:>2} {model_name}"
# #     print(item)

# display_main_divider()
# print()
# **************************************************


# **************************************************
import ollama

from dt_utility import (
    clear_screen,
    display_main_divider,
)

from rich import print
from ollama import ListResponse

clear_screen()
display_main_divider()

ollama_list: ListResponse = ollama.list()
models = ollama_list.models

model_names: list[str] = []
for model_item in models:
    if model_item.model:
        model_names.append(model_item.model)
model_names.sort()

for index, model_name in enumerate(model_names, start=1):
    item: str = f"{index:>2} {model_name}"
    print(item)

display_main_divider()
print()
# **************************************************
