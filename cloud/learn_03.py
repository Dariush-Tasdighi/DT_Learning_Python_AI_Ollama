# **************************************************
# Web Fetch
#
# https://docs.ollama.com/capabilities/web-search#web-fetch-api
# **************************************************
import sys

sys.path.append("..")

import os
import time
from ollama import Client
from dtx_dotenv import get_key_value

from rich import print
from rich.console import Console
from rich.markdown import Markdown

# BASE_URL: str = "https://ollama.com".strip().lower()
KEY_NAME_OLLAMA_API_KEY: str = "OLLAMA_API_KEY".strip().upper()


def main() -> None:
    """Main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    api_key: str = get_key_value(
        key=KEY_NAME_OLLAMA_API_KEY,
    )

    headers: dict = {"Authorization": f"Bearer {api_key}"}

    client = Client(
        # host=BASE_URL,
        headers=headers,
    )

    url: str = "https://ollama.com"
    # url: str = "https://example.com"

    # Step (1)
    response = client.web_fetch(url=url)

    print("=" * 50)
    print(response)
    print("=" * 50)
    # /Step (1)

    # Step (2)
    # response = client.web_fetch(url=url)

    # print("=" * 50)
    # print("Title:")
    # print(response.title)
    # print("-" * 50)
    # print("Content:")
    # print(response.content)
    # if response.links:
    #     print("-" * 50)
    #     print("Link(s):")
    #     for index, link in enumerate(response.links, start=1):
    #         print(f"{index}: {link}")
    # print("=" * 50)
    # /Step (2)

    # Step (3)
    # start_time: float = time.time()

    # response = client.web_fetch(url=url)

    # response_time: float = time.time() - start_time

    # print("=" * 50)
    # print("Title:")
    # print(response.title)
    # print("-" * 50)
    # if response.content:
    #     # print("Content:")
    #     console = Console()
    #     markdown = Markdown(response.content)
    #     console.print(markdown)
    # if response.links:
    #     print("-" * 50)
    #     print("Link(s):")
    #     for index, link in enumerate(response.links, start=1):
    #         print(f"{index}: {link}")
    # print("-" * 50)
    # print(f"Response Time: {response_time:.2f} seconds.")
    # print("=" * 50)
    # /Step (3)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print(f"[-] {error}!")

    print()
