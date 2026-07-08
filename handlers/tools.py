import uuid
import secrets
import string
import hashlib
import random

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
    length=None
    try:
        length = int(context.args[0]) if context.args else 16
        if not 8 <= length <= 64:
            await update.message.reply_text(
                "❌ Length must be between 8 and 64."
            )
            return
    except ValueError:
        await update.message.reply_text(
            "❌ Length must be a number.\n\nExample:\n/password 24"
        )
        return
    password = "".join(
        secrets.choice(alphabet)
        for _ in range(length)
    )

    await update.message.reply_text(
        f"🔐 Secure Password\n\n`{password}`",
        parse_mode="Markdown"
    )



async def hash_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text(
            "Usage:\n/hash <algorithm> <text>"
        )
        return

    algorithm = context.args[0].lower()

    if algorithm not in hashlib.algorithms_guaranteed:
        await update.message.reply_text(
            "❌ Unsupported algorithm."
        )
        return

    text = " ".join(context.args[1:])

    hashed = hashlib.new(
        algorithm,
        text.encode()
    ).hexdigest()

    await update.message.reply_text(
        f"🔒 {algorithm.upper()}\n\n`{hashed}`",
        parse_mode="Markdown"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args[0:])
    await update.message.reply_text(text)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong!\n\nStatus: Online ✅")