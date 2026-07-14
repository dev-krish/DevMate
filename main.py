from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from logger import logger

from handlers.info import (
    start,
    help_command,
    about,
)

from handlers.tools import (
    uuid_command,
    password_command,
    hash_command,
    echo,
    ping,
)

from handlers.chat import chat

from telegram.ext import CallbackQueryHandler

from handlers.callbacks import button_callback

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", help_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("uuid", uuid_command))
    app.add_handler(CommandHandler("password", password_command))
    app.add_handler(CommandHandler("hash", hash_command))
    app.add_handler(CommandHandler("echo",echo))
    app.add_handler(CallbackQueryHandler(button_callback))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )


    logger.info("🚀 DevMate started!")

    app.run_polling()


if __name__ == "__main__":
    main()