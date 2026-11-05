"""
Dictionary constants module.
"""

import dt_lm as utility

TEMPERATURE: float = 0.5
MODEL_NAME: str = "gemma3:12b".strip().lower()

# SYSTEM_PROMPT: str = """
# متن کاربر را به زبان فارسی ترجمه کن
# """

SYSTEM_PROMPT: str = """
تو یک مترجم حرفه‌ای از زبان انگلیسی، به زبان فارسی هستی.

- متن انگلیسی کاربر را با دقت، به زبان فارسی روان و برای کودکان ترجمه کن و از کلمات سخت و غیر مرسوم استفاده نکن.

- تمام آئین نگارش را در متن فارسی ترجمه شده، با دقت رعایت کن.

- در کلمات فارسی ترجمه شده، نیم فاصله را با دقت رعایت کن. یعنی مثلا به جای کلمه "می شود" بنویس "می‌شود" و یا به جای کلمه "درختها" بنویس "درخت‌ها".
"""

SYSTEM_PROMPT = SYSTEM_PROMPT.strip()
SYSTEM_MESSAGE: dict = {
    utility.KEY_NAME_ROLE: utility.ROLE_SYSTEM,
    utility.KEY_NAME_CONTENT: SYSTEM_PROMPT,
}

if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!")
