 
import configparser
import requests
import json

config=configparser.ConfigParser()
config.read("config.ini")
API_KEY=config['COINMARKETCAP']['API_KEY']
ALL_SYMBOLS_EP=config['COINMARKETCAP']['ALL_SYMBOLS_EP']
url=config['COINMARKETCAP']['ALL_SYMBOLS_EP']
url=url.format(API_KEY)
response=requests.get(url)
if response.status_code==200:
    currencies=json.loads(response.text)
    result=[]
    for i in range(0,12):
        text=currencies['data'][i]['name']
        result.append(text)
    print(result)    
    # for data in currencies['data'][data]['name']:
    #     text="{}".format(data)
    #     result.append(text)
    # print(result)
else:
    print('Se ha producido un error en la petición:',response.status_code)



