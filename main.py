import logging
# API keys were imported from here
import constants as keys
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

Image_key = "129c04"
url_base = "https://api.screenshotmachine.com?key="


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Hello! Send me the website you want me to screenshot for you. It can be a link or just the name")


def scheenshot(update: Update, context: CallbackContext) -> None:
    url = ""
    text = update.message.text.lower()

    if "http" in text:
        url = f"{url_base}{Image_key}&&url={text}&device=desktop&dimension=1024x768&format=png&cacheLimit=0&delay=0"
    elif not ".com" in text:
        url = f"{url_base}{Image_key}&&url=https%3A%2F%2F{text}.com&device=desktop&dimension=1024x768&format=png&cacheLimit=0&delay=0"
    else:
        url = f"{url_base}{Image_key}&&url=https%3A%2F%2F{text}&device=desktop&dimension=1024x768&format=png&cacheLimit=0&delay=0"
    update.message.reply_text("Looking for " + text)
    print("looking for "+text)
    update.message.reply_photo(
        url)


def main() -> None:
    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("scheenshot", scheenshot))
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, scheenshot))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
