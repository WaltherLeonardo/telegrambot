import logging
from telegram.ext import filters, ApplicationBuilder, CommandHandler, MessageHandler, InlineQueryHandler

from test2.constants import TOKEN
from functions import start, echo, caps, inline_caps, unknown

# This part is for setting up logging module,
# so I will know when (and why) things don't work as expected
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

application=ApplicationBuilder().token(TOKEN).build()

# here I've associated the /start commmand with the function
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
caps_handler = CommandHandler('caps', caps)
inline_caps_handler = InlineQueryHandler(inline_caps)
unknown_handler = MessageHandler(filters.COMMAND, unknown)

application.add_handler(start_handler)
application.add_handler(echo_handler)
application.add_handler(caps_handler)
application.add_handler(inline_caps_handler)
application.add_handler(unknown_handler)

application.run_polling()
