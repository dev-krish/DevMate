from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatAction, ParseMode
from logger import logger
from services.gemini_service import ask_gemini


async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/ask <your question>"
        )
        return

    prompt = " ".join(context.args)

    try:

        await update.message.chat.send_action(ChatAction.TYPING)

        answer = await ask_gemini(prompt)
    
        await update.message.reply_text(
            answer,
            parse_mode=ParseMode.HTML,
        )
    except Exception :

        logger.exception("AI Request Failed")

        await update.message.reply_text(
            "⚠️ Sorry! I couldn't contact the AI right now.\n"
            "Please try again in a moment."
        )