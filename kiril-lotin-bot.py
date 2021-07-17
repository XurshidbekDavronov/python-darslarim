# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:36:07 2021

@author: admin
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN='1790245700:AAGfXxNd3qKhwN3NqAAiZZjxngpTuwECVB0'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu alaykum, Xush kelibsiz!"
    javob+="\nMatn kiriting. Men kiritgan matningizni kirilldan lotinga yoki lotindan kirillga aylantirib beraman.Bo'lo'radimi?"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     javob=to_cyrillic(msg)
    # else:
    #     javob=to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()

# matn=input("Matn kiriting:")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
    # print(to_latin(matn))
