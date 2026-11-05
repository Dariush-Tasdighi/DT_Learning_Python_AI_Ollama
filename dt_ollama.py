"""
Dariush Tasdighi - Custom 'ollama' Package Utility Module
"""

import time

from typing import (
    Dict,
    List,
    Final,
    Tuple,
    Optional,
)

from ollama import (
    Client,
    ChatResponse,
)

from dt_lm import KEY_NAME_TEMPRETURE
from dt_utility import prevent_direct_execution

VERSION: Final[str] = "3.0.2"

MODEL_TEMPERATURE: Final[float] = 0.7
MODEL_NAME: Final[str] = "gemma4:e4b".replace(" ", "").lower()
BASE_URL: Final[str] = "http://127.0.0.1:11434".replace(" ", "").lower()


def chat(
    messages: List[Dict],
    think: bool = False,
    base_url: str = BASE_URL,
    model_name: str = MODEL_NAME,
    temperature: float = MODEL_TEMPERATURE,
) -> Tuple[Optional[str], float, int, int]:
    """Chat with Ollama service."""

    client = Client(host=base_url)

    start_time: float = time.perf_counter()

    response: ChatResponse = client.chat(
        think=think,
        stream=False,
        model=model_name,
        messages=messages,
        options={KEY_NAME_TEMPRETURE: temperature},
    )

    end_time: float = time.perf_counter()
    elapsed_time: float = end_time - start_time

    assistant_answer: Optional[str] = response.message.content

    prompt_tokens: int = 0  # Input Tokens
    completion_tokens: int = 0  # Output Tokens

    if assistant_answer:
        if response.eval_count is not None:
            completion_tokens = response.eval_count
        if response.prompt_eval_count is not None:
            prompt_tokens = response.prompt_eval_count

    return assistant_answer, elapsed_time, prompt_tokens, completion_tokens


if __name__ == "__main__":
    prevent_direct_execution()
