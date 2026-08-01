"""
Dictionary constants module.
"""

import dt_llm_utility as utility

TEMPERATURE: float = 0.2
# MODEL_NAME: str = "qwen2.5-coder:14b".replace(" ", "").lower()
MODEL_NAME: str = "qwen2.5-coder:1.5b".replace(" ", "").lower()

SYSTEM_PROMPT: str = """
You are a perfect developer with C# and .NET 9.

- You must create a model in EF Core based on user prompt.
- All properties must have XML documentation in Persian language.
- The list properties must be new with this shape: [] and must have 'virtual' keywords.
- The model must have primary constructor with all required properties.
- All models must be inherit from 'Entity' class.
- Just write properties that user told you, and never write anymore properties.
"""

SYSTEM_PROMPT = SYSTEM_PROMPT.strip()
SYSTEM_MESSAGE: dict = {
    utility.KEY_NAME_ROLE: utility.ROLE_SYSTEM,
    utility.KEY_NAME_CONTENT: SYSTEM_PROMPT,
}

if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!")
