import re
import os
import logging

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    update.message.reply_text('Start!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def screenshot(update: Update, context: CallbackContext) -> None:
    """Take a screenshot and send."""
    search = update.message.text

    # check if is a invalid URL for fix.
    if re.match(regex, search) is None:
        search = update.message.text
        search = f'https://www.{search}.com'

    update.message.reply_text("Searching...")

    # active headless option.
    options = Options()
    options.headless = True

    browser = webdriver.Firefox(
        options=options, executable_path=r'./geckodriver')

    # acess url.
    browser.get(search)
    # take screenshot.
    browser.save_screenshot('screenshot.png')

    # send screenshot.
    update.message.bot.send_photo(
        chat_id=update.effective_chat.id, photo=open('screenshot.png', 'rb'))


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv("TELEGRAM_KEY"))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, screenshot))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
