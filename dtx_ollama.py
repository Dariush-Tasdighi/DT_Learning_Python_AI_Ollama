"""
Dariush Tasdighi Custom 'ollama' Package Module
"""

import time
import logging
import dt_utility as utility
import dt_lm as llm_utility

from ollama import (
    Client,
    ChatResponse,
)

from typing import (
    Final,
    Optional,
)

from dtx_dotenv import get_key_value

VERSION: Final[str] = "3.0.1"

TEMPERATURE: Final[float] = 0.7

MODEL_NAME: Final[str] = "llama3.2:1b".replace(" ", "").lower()
BASE_URL_OFFLINE: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()

BASE_URL_ONLINE: Final[str] = "https://ollama.com".replace(" ", "").lower()
KEY_NAME_OLLAMA_API_KEY: Final[str] = "OLLAMA_API_KEY".replace(" ", "").lower()

logger = logging.getLogger(name=__name__)
logger.addHandler(hdlr=logging.NullHandler())


def get_offline_client(base_url: str = BASE_URL_OFFLINE) -> Client:
    """Get offline client"""

    client = Client(host=base_url)
    return client


def get_online_client() -> Client:
    """Get online client"""

    api_key: str = get_key_value(
        key=KEY_NAME_OLLAMA_API_KEY,
    )

    headers: dict = {"Authorization": f"Bearer {api_key}"}

    client = Client(
        headers=headers,
        host=BASE_URL_ONLINE,
    )

    return client


def chat(
    messages: list[dict],
    think: bool = False,
    model_name: str = MODEL_NAME,
    temperature: float = TEMPERATURE,
    base_url: str = BASE_URL_OFFLINE,
) -> tuple[Optional[str], float, int, int]:
    """Chat with Ollama service."""

    if model_name[-5:].lower() == "cloud":
        client = get_online_client()
    else:
        client = get_offline_client(base_url=base_url)

    logger.debug(msg=f"Ollama '{model_name}' chat started...")

    start_time: float = time.perf_counter()

    response: ChatResponse = client.chat(
        think=think,
        stream=False,
        model=model_name,
        messages=messages,
        options={llm_utility.KEY_NAME_TEMPRETURE: temperature},
    )

    end_time: float = time.perf_counter()
    elapsed_time: float = end_time - start_time

    logger.debug(msg=f"Ollama '{model_name}' chat finished.")

    assistant_answer: Optional[str] = response.message.content

    prompt_tokens: int = 0
    completion_tokens: int = 0

    if assistant_answer:
        if response.eval_count is not None:
            completion_tokens = response.eval_count
        if response.prompt_eval_count is not None:
            prompt_tokens = response.prompt_eval_count

    return assistant_answer, elapsed_time, prompt_tokens, completion_tokens


if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
