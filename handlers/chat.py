from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatAction, ParseMode
from logger import logger
from services.ai_service import ask_ai
from services.conversation_service import (
    get_history,
    save_message,
)

from utils.formatter import sanitize_html

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):


    try:

        await update.message.chat.send_action(ChatAction.TYPING)

        chat_id = update.effective_chat.id

        # Save the user's latest message
        save_message(
            chat_id,
            "user",
            update.message.text,
        )

        # Get updated conversation
        messages = get_history(chat_id)

        # Ask AI
        answer = await ask_ai(messages)
        
        # Save assistant reply
        save_message(
            chat_id,
            "assistant",
            answer,
        )
        answer = sanitize_html(answer)
        await update.message.reply_text(
            answer,
            parse_mode=ParseMode.HTML,
        )
        
    except Exception as e:

        logger.exception(f"AI Request Failed: {e}")

        await update.message.reply_text(
            "⚠️ Sorry! I couldn't contact the AI right now.\n"
            "Please try again in a moment."
        )