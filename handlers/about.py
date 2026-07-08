from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

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