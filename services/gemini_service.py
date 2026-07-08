from google import genai

from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def load_system_prompt():
    with open(
        "prompts/system_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()


# This executes ONCE when the application starts
SYSTEM_PROMPT = load_system_prompt()


async def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{SYSTEM_PROMPT}\n\nUser:\n{prompt}",
    )

    return response.text