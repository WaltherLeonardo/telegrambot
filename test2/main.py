import logging
from telegram import Update
from telegram.ext import filters, Application, CommandHandler, MessageHandler

from constants import TOKEN 
from functions import function_a, function_b, unknown

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

application = Application.builder().token(TOKEN).build()

admin_a = CommandHandler('a', function_a)
admin_b = CommandHandler('b', function_b)
unknown_handler = MessageHandler(filters.COMMAND, unknown)
application.add_handler(admin_a)
application.add_handler(admin_b)
application.add_handler(unknown_handler)

application.run_polling(allowed_updates=Update.ALL_TYPES)
