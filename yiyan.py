import requests
import Config


url = Config.config['hitokoto']

def get_hitokoto():

    data = {
        'c':'a'
    }
    req = requests.get(url, params=data)
    rs = dict(req.json())
    return str(rs['hitokoto']+'——  '+rs['from'])

print(get_hitokoto())