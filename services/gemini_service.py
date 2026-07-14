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
    
async def ask_gemini(messages: list[dict]) -> str:
    conversation = SYSTEM_PROMPT + "\n\n"

    for message in messages:

        if message["role"] == "user":
            conversation += f"User: {message['content']}\n"

        elif message["role"] == "assistant":
            conversation += f"Assistant: {message['content']}\n"

        conversation += "\nAssistant:"    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation,
    )

    return response.text