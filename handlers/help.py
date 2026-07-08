from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
        🤖 DevMate Help

        Welcome to DevMate! Here are the available commands:

        🧰 Developer Tools
        /uuid - Generate a UUID
        /password [length] - Generate a secure password
        /hash <text> - Generate a SHA-256 hash
        /echo <text> - Echo back your message

        ℹ️ Information
        /start - Start DevMate
        /help - Show this help menu
        /about - Learn more about DevMate

        💬 AI Chat

        Simply send any message without a command to chat with DevMate.

        Examples:
        • Hello
        • Explain Docker
        • Write a Python function to reverse a linked list
        • What's the difference between SQL and MongoDB?
    """

    await update.message.reply_text(help_text)