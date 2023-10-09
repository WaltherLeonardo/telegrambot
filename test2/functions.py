from telegram import Update
from telegram.ext import ContextTypes

async def function_a(update:Update, context:ContextTypes.DEFAULT_TYPE ):
    await update.message.reply_text("option a chosen")

async def function_b(update:Update, context:ContextTypes.DEFAULT_TYPE ):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="option b chosen")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry,I didn't understand that command")