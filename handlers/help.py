from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
    🛠️ DevMate v0.1

    Available Commands

    🚀 Basic
    /start - Start the bot
    /help - Show this help menu
    /about - About DevMate
    /ping - Check if the bot is online

    💬 Utilities
    /echo - Echo your message

    More developer tools coming soon...
    """

    await update.message.reply_text(help_text)