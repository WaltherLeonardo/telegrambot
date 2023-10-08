import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

from constants import TOKEN 
from functions import function_a

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)


application = Application.builder().token(TOKEN).build()

admin_message = MessageHandler(callback=function_a, filters=filters.ALL)
application.add_handler(admin_message)

# run
application.run_polling(allowed_updates=Update.ALL_TYPES)