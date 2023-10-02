import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

from functions3 import start, start_over, one, two, three, four, end
from constants import TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

START_ROUTES, END_ROUTES = range(2)
ONE, TWO, THREE, FOUR = range(4)

application = Application.builder().token(TOKEN).build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        START_ROUTES: [
            CallbackQueryHandler(one, pattern="^" + str(ONE) + "$"),
            CallbackQueryHandler(two, pattern="^" + str(TWO) + "$"),
            CallbackQueryHandler(three, pattern="^" + str(THREE) + "$"),
            CallbackQueryHandler(four, pattern="^" + str(FOUR) + "$"),
        ],
        END_ROUTES: [
            CallbackQueryHandler(start_over, pattern="^" + str(ONE) + "$"),
            CallbackQueryHandler(end, pattern="^" + str(TWO) + "$"),
        ],
    },
    fallbacks=[CommandHandler("start", start)],
)

application.add_handler(conv_handler)
application.run_polling(allowed_updates=Update.ALL_TYPES)
