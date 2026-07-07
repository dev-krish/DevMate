import uuid
import secrets
import string

from telegram import Update
from telegram.ext import ContextTypes


async def uuid_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    generated_uuid = uuid.uuid4()

    await update.message.reply_text(
        f"🆔 Generated UUID\n\n`{generated_uuid}`",
        parse_mode="Markdown"
    )

async def password_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    alphabet = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*"
    )

    password = "".join(
        secrets.choice(alphabet)
        for _ in range(16)
    )

    await update.message.reply_text(
        f"🔐 Secure Password\n\n`{password}`",
        parse_mode="Markdown"
    )