import telebot
#from telebot import types

bot = telebot.Telebot('5259869971:AAG8E07VuKAU5RXgYgM8IJIoijDCkt0UZHA')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем могу помочь?")
    elif message.text =="/help":
        bot.send_message(message.from_user.id, "Напиши help")

