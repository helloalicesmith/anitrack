from dotenv import load_dotenv
import os
import logging

from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram import Update, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler

from mapping import map_inline_keyboard_buttons
from config import inline_keyboard_button

load_dotenv()

token = os.environ['TOKEN']
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)


def start(update: Update, context: CallbackContext):
    buttons = map_inline_keyboard_buttons(inline_keyboard_button)

    update.message.reply_text(
        'Please choose:', reply_markup=InlineKeyboardMarkup(buttons))


def query_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    handler = inline_keyboard_button[query.data]['handler']
    handler()


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(query_handler))

updater.start_polling()
