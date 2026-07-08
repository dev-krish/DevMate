from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


async def ask_gemini(prompt: str) -> str:
    system_prompt = f"""
        You are DevMate, an AI developer assistant inside Telegram.

        Rules:
        - Be concise.
        - Prefer code examples when useful.
        - Use Markdown formatting.
        - Answer programming questions accurately.
        - If the user asks a non-programming question, still answer helpfully.

        User:
        {prompt}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=system_prompt,
    )

    return response.text