import configparser
import requests
import json

config=configparser.ConfigParser()
config.read("config.ini")


API_KEY=config['COINMARKETCAP']['API_KEY']

inSymbol=input('¿Qué moneda quieres convertir?')
outSymbol=input('¿En qué otra moneda?')

url=config['COINMARKETCAP']['RATE_LATEST_EP']
url=url.format(inSymbol,outSymbol,API_KEY)
response=requests.get(url)
if response.status_code==200:
    print(response.text)
else:
    print('Se ha producido un error en la petición:',response.status_code)
