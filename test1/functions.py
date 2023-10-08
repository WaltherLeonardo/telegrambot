# functions

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ContextTypes

# /start commnad
async def start(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="return answer to start command")

# respond the same 
async def echo(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# /cap commnad
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps= ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

# inline: from another chat I can invoque a functions
async def inline_caps(update: Update, context:ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results=[]
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

# defaul answer
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry,I didn't understand that command")

