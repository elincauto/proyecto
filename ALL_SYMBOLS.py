 
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
    """ result=[]
    symbols=currencies['symbols']
    for symbol in symbols:
        text="{}-{}".format(symbol,symbols[symbol])
        result.append(text)
    print(result) """
    #print(currencies)

else:
    print('Se ha producido un error en la petición:',response.status_code)



