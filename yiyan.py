import requests
import Config


url = Config.config['hitokoto']

def get_hitokoto():

    req = requests.get(url)
    rs = dict(req.json())
    return str(rs['hitokoto']+'------- '+rs['from'])

print(get_hitokoto())