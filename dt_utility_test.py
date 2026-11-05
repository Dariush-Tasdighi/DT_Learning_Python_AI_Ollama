from rich import print
from ollama import ListResponse

from dt_utility import (
    clear_screen,
    display_divider,
    get_formated_now,
    display_main_divider,
    display_error_message,
    display_title_message,
    display_success_message,
    display_information_message,
)

clear_screen()

display_main_divider()
display_error_message(message="Error message")
display_divider()
display_title_message(message="Title message")
display_divider()
display_success_message(message="Success message")
display_divider()
display_information_message(message="Information message")
display_divider()
print(get_formated_now())
print(get_formated_now(with_miliseconds=True))
display_main_divider()
print()
