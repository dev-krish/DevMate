from ollama import chat

from config import OLLAMA_MODEL

def load_system_prompt():
    with open(
        "prompts/system_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()

# This executes ONCE when the application starts
SYSTEM_PROMPT = load_system_prompt()

async def ask_ollama(messages: list[dict]) -> str:
        
    response = chat(
        model=OLLAMA_MODEL,
        messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },
                    *messages,
                ],
    )

    return response["message"]["content"]