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
                "Welcome! 🚀 I'm your digital co-pilot , DevMate!👋.\n\nI'm ready to help.\nWhether you need to crush your daily goals, debug a tricky piece of code, or just chat about life, I've got you covered.\n\nLet's have a Chat?💭",
                parse_mode=ParseMode.HTML,
            )

        case "help":
            await query.message.reply_text(
                "❓ <b>Quick Help</b>\n\n"
                "• Simply send a message to chat with DevMate.\n"
                "• Use /clear - Clear the current conversation memory. \n"
                "• Use /password to generate passwords.\n"
                "• Use /hash to generate SHA-256 hashes.\n"
                "• Use /uuid to generate UUIDs.",
                parse_mode=ParseMode.HTML,
            )