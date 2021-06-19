# -*- coding: utf-8 -*-
import time

import telebot
import Config

token = '1829725347:AAGEUC1uVH5PLfbN5s1Wu645SG2Qtwdzr8A'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text='你寄吧谁！')


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

if __name__=='__main__':

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(2)