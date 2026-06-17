"""
Dariush Tasdighi Custom 'ollama' Package Module
"""

from typing import Final
from typing import Optional

from ollama import Client
from ollama import ChatResponse

import dt_utility as utility
import dt_llm_utility as llm_utility

VERSION: Final[str] = "2.3"

TEMPERATURE: Final[float] = 0.7
MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()
BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()


def chat(
    messages: list[dict],
    think: bool = False,
    notify: bool = False,
    base_url: str = BASE_URL,
    model_name: str = MODEL_NAME,
    temperature: float = TEMPERATURE,
) -> tuple[Optional[str], int, int]:
    """Chat with Ollama service."""

    client = Client(host=base_url)

    if notify:
        utility.display_information_message(
            message=f"Ollama '{model_name}' chat started...",
        )

    response: ChatResponse = client.chat(
        think=think,
        stream=False,
        model=model_name,
        messages=messages,
        options={llm_utility.KEY_NAME_TEMPRETURE: temperature},
    )

    if notify:
        utility.display_information_message(
            message=f"Ollama '{model_name}' chat finished.",
        )

    assistant_answer: Optional[str] = response.message.content

    prompt_tokens: int = 0
    completion_tokens: int = 0

    if assistant_answer:
        if response.eval_count:
            completion_tokens = response.eval_count
        if response.prompt_eval_count:
            prompt_tokens = response.prompt_eval_count

    return assistant_answer, prompt_tokens, completion_tokens


if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
