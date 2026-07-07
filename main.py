from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import MessageHandler, filters
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN =os.getenv("BOT_TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm your first Telegram bot 🚀"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

async def hello(update, context):
    await update.message.reply_text("Hello Krish!")

app.add_handler(CommandHandler("hello", hello))


async def echo(update, context):
    await update.message.reply_text(update.message.text)

app.add_handler(MessageHandler(filters.TEXT, echo))

app.run_polling()