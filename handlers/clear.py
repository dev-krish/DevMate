from telegram import Update
from telegram.ext import ContextTypes

from services.conversation_service import clear_history


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    clear_history(chat_id)

    await update.message.reply_text(
        "🧹 Conversation memory cleared!\n\n"
        "Let's start a fresh conversation. 🚀"
    )