from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN

from handlers.start import start
from handlers.help import help_command
from handlers.echo import echo
from handlers.help import help_command
from handlers.about import about
from handlers.ping import ping
from handlers.tools import uuid_command
from handlers.tools import password_command

app = ApplicationBuilder().token(BOT_TOKEN).build()

# Commands
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", help_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("uuid", uuid_command))
app.add_handler(CommandHandler("password", password_command))

# Messages
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("🚀 DevMate is running...")

app.run_polling()