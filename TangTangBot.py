# import telebot
#
# import Config
#
# class TangBot(object):
#     def __init__(self):
#             self.token = Config.config['TOKEN']
#             self.bot = telebot.TeleBot(self.token, parse_mode=None)
#
#     def bot_main(self):
#         # 获取最新消息
#         update = self.bot.get_updates()
#         # print(update)
#         if update is None:
#             return "Show me your TOKEN please!"
#         logging.info("Calling {}".format(update.message))
#         self.handdle_message(update.message)
#         return "ok"
#     def handdle_message(self, message):
#         if(message.content_types=='text):
#             self.echo(message)
#         return
#     def echo(self, message):
#         self.bot.reply_to(message.chat.id, message.text)
