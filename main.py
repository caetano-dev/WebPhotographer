import logging
# API keys were imported from here
import constants as keys
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def ufrrj(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Let me check")
    update.message.reply_photo(
        "https://api.screenshotmachine.com?key=129c04&url=https%3A%2F%2Fr1.ufrrj.br%2Fsisu%2F3-lista-de-espera%2Fmanifestacao-de-interesse%2F&device=desktop&dimension=1024x768&format=png&cacheLimit=0&delay=0")


def scheenshot(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    update.message.reply_text("Looking for " + text)
    update.message.reply_photo(
        f"https://api.screenshotmachine.com?key=129c04&url=https%3A%2F%2F{text}.com&device=desktop&dimension=1024x768&format=png&cacheLimit=0&delay=0")


def main() -> None:
    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("ufrrj", ufrrj))
    dispatcher.add_handler(CommandHandler("scheenshot", scheenshot))
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, scheenshot))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
