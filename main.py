import telebot
import screenshot
import asyncio
import os

bot = telebot.TeleBot("API KEY GOES HERE", parse_mode=None)


@bot.message_handler(commands=["hello"])
def greet(message):
    print("hello")
    bot.reply_to((message), "what's up?")


@bot.message_handler(commands=["website"])
async def website(message):
    asyncio.get_event_loop().run_until_complete(screenshot())
    bot.send_message((message.chat.id), "I'll check it")
    bot.send_photo((message.chat.id), photo=open("./webScreenshot.png", "rb"))
    os.remove("./webScreenshot.png")

bot.polling()
