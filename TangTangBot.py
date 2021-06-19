# -*- coding: utf-8 -*-
import time

import telebot
from telebot.apihelper import send_data
import Config
from yiyan import *

token = Config.config['TOKEN']

bot = telebot.TeleBot(token)

# /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text='你寄吧谁！')

# 回声
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

# 一言
@bot.message_handler(commands=['hitokoto'])
def hitokoto1(message):
    sentence = get_hitokoto()
    bot.send_message(message.chat.id, text=sentence )

@bot.message_handler(content_types=['text'])
def hitokoto2(message):
    if(message.text == '一言'):
        try:
            sentence = get_hitokoto()
            bot.send_message(message.chat.id, text=sentence)
        except Exception as e:
            return


if __name__=='__main__':

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(2)