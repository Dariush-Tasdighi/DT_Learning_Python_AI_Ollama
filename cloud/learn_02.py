# **************************************************
# Web Search
#
# https://docs.ollama.com/capabilities/web-search
# **************************************************
import sys

sys.path.append("..")

import os
import time
from rich import print
from ollama import Client
from dtx_dotenv import get_key_value

# فعلا به دستور ذیل احتیاج ندارد
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

    query: str = "What is AI Agent?"

    # Step (1)
    response = client.web_search(
        query=query,
        max_results=3,  # Default: 3, Max: 10
    )

    print("=" * 50)
    print(response)
    print("=" * 50)
    # /Step (1)

    # Step (2)
    # response = client.web_search(
    #     query=query,
    #     max_results=3,  # Default: 3, Max: 10
    # )

    # print("=" * 50)
    # print(f"Result Count: {len(response.results)}")
    # print("=" * 50)
    # print()
    # for index, result in enumerate(response.results):
    #     print("-" * 50)
    #     print(f"Result: [{index + 1}]")
    #     print()
    #     print("Title:")
    #     print(result.title)
    #     print()
    #     print("URL:")
    #     print(result.url)
    #     print()
    #     print("Content:")
    #     if result.content:
    #         print(result.content[:50])
    #     print("-" * 50)
    #     print()
    # /Step (2)

    # Step (3)
    # start_time: float = time.time()

    # response = client.web_search(
    #     query=query,
    #     max_results=3,  # Default: 3, Max: 10
    #     # max_results=10,  # Default: 3, Max: 10
    #     # max_results=100,  # Default: 3, Max: 10
    # )

    # response_time: float = time.time() - start_time

    # print("=" * 50)
    # print(f"Result Count: {len(response.results)}")
    # print("-" * 50)
    # print(f"Response Time: {response_time:.2f} seconds.")
    # print("=" * 50)
    # print()
    # for index, result in enumerate(response.results):
    #     print("-" * 50)
    #     print(f"Result: [{index + 1}]")
    #     print()
    #     print("Title:")
    #     print(result.title)
    #     print()
    #     print("URL:")
    #     print(result.url)
    #     print()
    #     print("Content:")
    #     if result.content:
    #         print(result.content[:50])
    #     print("-" * 50)
    #     print()
    # /Step (3)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print(f"[-] {error}!")

    print()
