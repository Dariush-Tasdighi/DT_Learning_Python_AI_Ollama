# **************************************************
# import os

# # نیازی به نصب ندارد
# import json
# from rich import print

# os.system(command="cls" if os.name == "nt" else "clear")

# messages: list[dict] = []

# SYSTEM_PROMPT: str = "System Prompt"
# SYSTEM_MESSAGE: dict = {"role": "system", "content": SYSTEM_PROMPT}
# messages.append(SYSTEM_MESSAGE)

# user_prompt: str = "User Prompt (1)"
# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# assistant_answer: str = "Assistant Answer (1)"
# assistant_message: dict = {"role": "assistant", "content": assistant_answer}
# messages.append(assistant_message)

# user_prompt = "User Prompt (2)"
# user_message = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# assistant_answer = "Assistant Answer (2)"
# assistant_message = {"role": "assistant", "content": assistant_answer}
# messages.append(assistant_message)

# user_prompt = "User Prompt (3)"
# user_message = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# assistant_answer = "Assistant Answer (3)"
# assistant_message = {"role": "assistant", "content": assistant_answer}
# messages.append(assistant_message)

# print("=" * 50)
# print(messages)

# # Serialization: Object to Json String
# json_string: str = json.dumps(
#     messages,
#     indent=4,
#     default=lambda o: o.__dict__,
# )

# print("-" * 50)
# print(json_string)

# # Deserialization: Json String to Object
# new_messages: list[dict] = json.loads(s=json_string)

# print("-" * 50)
# print(new_messages)
# print("=" * 50)
# **************************************************


# **************************************************
# import os
# import json
# from rich import print

# JSON_FILE_PATH: str = "./data/data.json"

# os.system(command="cls" if os.name == "nt" else "clear")

# messages: list[dict] = []

# SYSTEM_PROMPT: str = "System Prompt"
# SYSTEM_MESSAGE: dict = {"role": "system", "content": SYSTEM_PROMPT}
# messages.append(SYSTEM_MESSAGE)

# user_prompt: str = "User Prompt (1)"
# user_message: dict = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# assistant_answer: str = "Assistant Answer (1)"
# assistant_message: dict = {"role": "assistant", "content": assistant_answer}
# messages.append(assistant_message)

# user_prompt = "User Prompt (2)"
# user_message = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# assistant_answer = "Assistant Answer (2)"
# assistant_message = {"role": "assistant", "content": assistant_answer}
# messages.append(assistant_message)

# user_prompt = "User Prompt (3)"
# user_message = {"role": "user", "content": user_prompt}
# messages.append(user_message)

# assistant_answer = "Assistant Answer (3)"
# assistant_message = {"role": "assistant", "content": assistant_answer}
# messages.append(assistant_message)

# print("=" * 50)
# print(messages)

# json_string: str = json.dumps(
#     messages,
#     indent=4,
#     default=lambda o: o.__dict__,
# )

# # Bad Practice
# # file = open(file=JSON_FILE_PATH, mode="wt", encoding="utf-8")
# # file.write(json_string)
# # file.close()

# # Best Practice
# with open(file=JSON_FILE_PATH, mode="wt", encoding="utf-8") as file:
#     file.write(json_string)

# with open(file=JSON_FILE_PATH, mode="rt", encoding="utf-8") as file:
#     new_json_string: str = file.read()

# print("-" * 50)
# print(new_json_string)

# new_messages: list[dict] = json.loads(s=new_json_string)

# print("-" * 50)
# print(new_messages)
# print("=" * 50)
# **************************************************


# **************************************************
import os
import json
from typing import Any
from rich import print

JSON_FILE_PATH: str = "./data/data.json"


def save_text_file(text: str, file_path: str) -> None:
    """Save text file."""

    with open(file=file_path, mode="wt", encoding="utf-8") as file:
        file.write(text)


def load_text_file(file_path: str) -> str | None:
    """Load text file."""

    if not os.path.exists(path=file_path):
        return None

    if not os.path.isfile(path=file_path):
        return None

    with open(file=file_path, mode="rt", encoding="utf-8") as file:
        text: str = file.read()
        return text


def serialize_and_save(obj, file_path: str) -> None:
    """Serialize and save."""

    json_string: str = json.dumps(
        obj,
        indent=4,
        default=lambda o: o.__dict__,
    )

    save_text_file(
        text=json_string,
        file_path=file_path,
    )


def load_and_deserialize(file_path: str) -> Any:
    """Load and deserialize."""

    text: str | None = load_text_file(file_path=file_path)

    if text == None:
        return None

    result = json.loads(s=text)
    return result


os.system(command="cls" if os.name == "nt" else "clear")

messages: list[dict] = []

SYSTEM_PROMPT: str = "System Prompt"
SYSTEM_MESSAGE: dict = {"role": "system", "content": SYSTEM_PROMPT}
messages.append(SYSTEM_MESSAGE)

user_prompt: str = "User Prompt (1)"
user_message: dict = {"role": "user", "content": user_prompt}
messages.append(user_message)

assistant_answer: str = "Assistant Answer (1)"
assistant_message: dict = {"role": "assistant", "content": assistant_answer}
messages.append(assistant_message)

user_prompt = "User Prompt (2)"
user_message = {"role": "user", "content": user_prompt}
messages.append(user_message)

assistant_answer = "Assistant Answer (2)"
assistant_message = {"role": "assistant", "content": assistant_answer}
messages.append(assistant_message)

user_prompt = "User Prompt (3)"
user_message = {"role": "user", "content": user_prompt}
messages.append(user_message)

assistant_answer = "Assistant Answer (3)"
assistant_message = {"role": "assistant", "content": assistant_answer}
messages.append(assistant_message)

print("=" * 50)
print(messages)

serialize_and_save(
    obj=messages,
    file_path=JSON_FILE_PATH,
)

result = load_and_deserialize(
    file_path=JSON_FILE_PATH,
)

if result:
    new_messages: list[str] = result

    print("-" * 50)
    print(new_messages)
    print("=" * 50)
# **************************************************
