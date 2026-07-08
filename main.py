from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from logger import logger

from handlers.start import start
from handlers.help import help_command
from handlers.echo import echo
from handlers.about import about
from handlers.ping import ping
from handlers.tools import (
    uuid_command,
    password_command,
    hash_command,
)
from handlers.ask import ask

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

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    app.add_handler(CommandHandler("ask", ask))
    
    logger.info("🚀 DevMate started!")

    app.run_polling()


if __name__ == "__main__":
    main()