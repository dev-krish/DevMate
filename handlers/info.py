from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "💬 Start Chat",
                callback_data="start_chat",
            )
        ],
        [
            InlineKeyboardButton(
                "🧹 Clear Memory",
                callback_data="clear_memory",
            )
        ],
        [
            InlineKeyboardButton(
                "❓ Help",
                callback_data="help",
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text="""
        🤖 Welcome to DevMate!🚀

        Your AI Developer Companion 🫂
        Or Maybe Your Chat buddy ? 😉

        Choose an option below 👇😃
    """
    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
    )


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


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = """
        🤖 <b>About DevMate</b>

        DevMate is an AI-powered developer assistant built to help developers directly inside Telegram.

        ✨ <b>Features</b>
        • AI-powered conversations
        • Secure password generation
        • SHA-256 hashing
        • UUID generation
        • Dockerized deployment
        • Cloud deployment on Render
        • Local AI support with Ollama
        • Cloud AI support with Gemini

        🛠 <b>Tech Stack</b>
        Python • python-telegram-bot • Docker • Gemini • Ollama

        👨‍💻 Built with ❤️ by Krishnendu Dutta

        🚀 Version: v0.2.0
        """

    await update.message.reply_text(
        about_text,
        parse_mode=ParseMode.HTML,
    )