from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from services.conversation_service import clear_history


async def button_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    await query.answer()

    chat_id = query.message.chat.id

    match query.data:

        case "start_chat":
            await query.message.reply_text(
                "💬 <b>Conversation Started!</b>\n\n"
                "I'm ready to help.\n"
                "Ask me anything about programming, AI, Docker, or software development.",
                parse_mode=ParseMode.HTML,
            )

        case "clear_memory":
            clear_history(chat_id)

            await query.message.reply_text(
                "🧹 <b>Conversation memory cleared.</b>\n\n"
                "Let's start fresh! 🚀",
                parse_mode=ParseMode.HTML,
            )

        case "help":
            await query.message.reply_text(
                "❓ <b>Quick Help</b>\n\n"
                "• Simply send a message to chat with DevMate.\n"
                "• Use /password to generate passwords.\n"
                "• Use /hash to generate SHA-256 hashes.\n"
                "• Use /uuid to generate UUIDs.",
                parse_mode=ParseMode.HTML,
            )