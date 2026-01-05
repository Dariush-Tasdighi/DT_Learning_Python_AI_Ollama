# **************************************************
"""
Generate TSQL Assistant (Offline).
"""

import os
import time
from rich import print
from dt_ollama import chat
import dt_llm_utility as utility
from rich.console import Console
from rich.markdown import Markdown

TEMPERATURE: float = 0

MODEL_NAME: str = "qwen2.5-coder:14b".strip().lower()

# SYSTEM_PROMPT: str = "You are a helpful AI assistant."

SYSTEM_PROMPT: str = """
You are a professional TSQL generator.

User must write just TSQL script based on below structure of tables:

Table Name: SaleInvoiceDetails
    Field Name: SaleInvoiceId
    Field Name: ProductId
    Field Name: Quantity
    Field Name: UnitPrice
    Field Name: TotalPrice
    Field Name: Discount
    Field Name: Tax
    Field Name: Weight
Table Name: Products
    Field Name: ProductId
    Field Name: ProductCode
    Field Name: ProductName
    Field Name: UnitPrice
"""

SYSTEM_PROMPT = SYSTEM_PROMPT.strip()
SYSTEM_MESSAGE: dict = {
    utility.KEY_NAME_ROLE: utility.ROLE_SYSTEM,
    utility.KEY_NAME_CONTENT: SYSTEM_PROMPT,
}


def main() -> None:
    """The main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    print("=" * 50)
    user_prompt: str = """
    با توجه به ساختار جداول بانک اطلاعاتی، لطفا صرفا یک TSQL بنویس که:
    تعداد کالاهای فروش رفته به تفکیک نام کالا
    """

    user_prompt = user_prompt.strip()

    messages: list[dict] = []
    messages.append(SYSTEM_MESSAGE)

    user_message: dict = {
        utility.KEY_NAME_ROLE: utility.ROLE_USER,
        utility.KEY_NAME_CONTENT: user_prompt,
    }

    messages.append(user_message)

    start_time: float = time.time()

    assistant_answer, prompt_tokens, completion_tokens = chat(
        messages=messages,
        model_name=MODEL_NAME,
        temperature=TEMPERATURE,
    )

    response_time: float = time.time() - start_time

    if not assistant_answer:
        assistant_answer = utility.MESSAGE_NO_CONTENT_RECEIVED

    print("-" * 50)
    console = Console()
    markdown = Markdown(markup=assistant_answer)
    console.print(markdown)
    print("-" * 50)
    print("Prompt Tokens (Input):", prompt_tokens)
    print("-" * 50)
    print("Completion Tokens (Output):", completion_tokens)
    print("-" * 50)
    print(f"Full response received {response_time:.2f} seconds after request.")
    print("=" * 50)
    print()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()

    except Exception as error:
        print(f"\n[-] {error}!")

    print()
