import time

from logger import logger

from config import AI_PROVIDER

from services.gemini_service import ask_gemini
from services.ollama_service import ask_ollama


PROVIDERS = {
    "gemini": ask_gemini,
    "ollama": ask_ollama,
}


async def ask_ai(prompt: str) -> str:

    provider = AI_PROVIDER.lower()

    if provider not in PROVIDERS:
        raise ValueError(f"Unsupported AI provider: {provider}")

    logger.info(f"Using AI Provider: {provider}")

    start = time.perf_counter()

    answer = await PROVIDERS[provider](prompt)

    elapsed = time.perf_counter() - start

    logger.info(f"Response generated in {elapsed:.2f}s")

    return answer