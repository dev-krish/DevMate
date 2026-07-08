from ollama import chat

from config import OLLAMA_MODEL


async def ask_ollama(prompt: str) -> str:

    response = chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    return response["message"]["content"]