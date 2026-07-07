from telegram import Update
from telegram.ext import ContextTypes

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = """
🤖 DevMate

Your Developer Companion.

Built with ❤️ using Python.

Version: 0.1.0

Creator: Krishnendu Dutta
"""

    await update.message.reply_text(about_text)