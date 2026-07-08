from telegram import Update
from telegram.ext import ContextTypes

from services.gemini_service import ask_gemini


async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/ask <your question>"
        )
        return

    prompt = " ".join(context.args)

    await update.message.chat.send_action("typing")

    answer = await ask_gemini(prompt)

    await update.message.reply_text(answer)