from flask import Flask
import threading
import time
from TangTangBot import *

status = ""

app = Flask(__name__)


@app.route('/bot', methods=['GET'])
def bot_info():
    try:
        print(bot.get_me())
        return str(bot.get_me())
    except:
        return "无法获取bot信息，请检查api token"

def run_bot():

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(10)

@app.route('/', methods=['GET'])
def index():
    global status
    if status=="":
        t1 = threading.Thread(target=run_bot)
        t1.start()
        print(t1.is_alive())
        status = t1
        return "正在唤醒Bot", 200
    else:
        print(status.is_alive())
        if status.is_alive() == True:
            return "Bot 已经在运行"
        elif status.is_alive() == False:
            t1 = threading.Thread(target=run_bot)
            t1.start()
            print(t1.is_alive())
            status=t1
            return "重新唤醒Bot", 200

if __name__ == '__main__':
    app.run(debug=True)
