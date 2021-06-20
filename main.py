import telebot
import screenshot
bot = telebot.TeleBot("API CODE HERE", parse_mode=None)

@bot.message_handler(commands=["hello"])
def greet(message):
	bot.reply_to((message),"what's up?")

@bot.message_handler(commands=["ufrrj"])
def greet(message):
	bot.send_message((message.chat.id),"I'll check it")
	screenshot()

bot.polling()