"""
Dariush Tasdighi Ollama module.
"""

import logging
from rich import print
from ollama import Client
from ollama import ChatResponse
import dt_llm_utility as utility
from dtx_dotenv import get_key_value

__version__ = "1.0"

logger = logging.getLogger(name=__name__)
logger.addHandler(hdlr=logging.NullHandler())

TEMPERATURE: float = 0.7
KEY_NAME_OLLAMA_API_KEY: str = "OLLAMA_API_KEY".strip().upper()

MODEL_NAME_OFFLINE: str = "gemma3:1b".strip().lower()
BASE_URL_OFFLINE: str = "http://127.0.0.1:11434".strip().lower()

MODEL_NAME_ONLINE: str = "gpt-oss:20b-cloud".strip().lower()
BASE_URL_ONLINE: str = "https://ollama.com".strip().lower()

SYSTEM_PROMPT: str = "You are a helpful AI assistant."

SYSTEM_MESSAGE: dict = {
    utility.KEY_NAME_ROLE: utility.ROLE_SYSTEM,
    utility.KEY_NAME_CONTENT: SYSTEM_PROMPT,
}


def get_client_offline(base_url: str = BASE_URL_OFFLINE) -> Client:
    """Get client (offline)"""

    client = Client(
        host=base_url,
    )

    return client


def get_client_online() -> Client:
    """Get client (online)"""

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
    base_url: str = BASE_URL_OFFLINE,
    model_name: str = MODEL_NAME_OFFLINE,
    temperature: float = TEMPERATURE,
) -> tuple[str | None, int, int]:
    """Chat with Ollama"""

    if model_name[-5:].lower() == "cloud":
        client = get_client_online()
    else:
        client = get_client_offline(base_url=base_url)

    logger.debug(msg=f"Ollama '{model_name}' chat started...")

    response: ChatResponse = client.chat(
        think=think,
        stream=False,
        model=model_name,
        messages=messages,
        options={utility.KEY_NAME_TEMPRETURE: temperature},
    )

    logger.debug(msg=f"Ollama '{model_name}' chat finished.")

    assistant_answer: str | None = response.message.content

    prompt_tokens: int = 0
    completion_tokens: int = 0

    if assistant_answer:
        if response.eval_count:
            completion_tokens = response.eval_count
        if response.prompt_eval_count:
            prompt_tokens = response.prompt_eval_count

    return assistant_answer, prompt_tokens, completion_tokens


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!")
