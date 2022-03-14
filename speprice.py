from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
import colorama
from colorama import Fore
from colorama import Style
from twilio.rest import Client 

colorama.init()

dev = " R$0.05"
global ok
global confere

def request():
    global content
    html = requests.get("https://coinmarketcap.com/pt-br/currencies/space-crypto-spe/").content
    '''html_dec = html.read().decode(encoding="iso-8859-1")'''
    bs = BeautifulSoup(html, 'html.parser')

    #Procura pelo elemento div que mostra o preço do token na página estática
    aim = bs.find("div", class_="priceValue")
    content = aim.string

request()

if content >= 'R$0,20':
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + '"{}"'.format(content) + Style.RESET_ALL + ' Preço atual do token')
elif content >= 'R$0.15' and content < 'R$0.20':
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '"{}"'.format(content) + Style.RESET_ALL + ' Preço atual do token')
elif content <= 'R$0.10':
    print(Fore.LIGHTRED_EX + Style.BRIGHT + '"{}"'.format(content) + Style.RESET_ALL + ' Preço atual do token')

def _main_():
    global ok
    global confere
    while True:
        request()
        count = []
        print('--------------------)\n')
        print('Atualizando:')
        print('...')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('...\n')
        time.sleep(0.5)
        print('--------------------\n')
        time.sleep(0.2)
        if content >= 'R$0.20':
            time.sleep(0.5)
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + '"{}"'.format(content) + Style.RESET_ALL + ' Novo preço do token\n')
            time.sleep(0.5)
        elif content >= 'R$0.15' and content < 'R$0.20':
            time.sleep(0.5)
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '"{}"'.format(content) + Style.RESET_ALL + ' Novo preço do token\n')
            time.sleep(0.5)
        elif content <= 'R$0.14' and content >= 'R$0.10':
            time.sleep(1)
            print(Fore.LIGHTRED_EX + Style.BRIGHT + '"{}"'.format(content) + Style.RESET_ALL + ' Novo Preço do token\n')
            time.sleep(0.5)
        elif content <= 'R$0.06':
            account_sid = 'ACa4ae46a23ee183f2c9ffabdc3125b8de'
            auth_token = '49d1c04a9c4c70a001bd0511c580f1d5'
            client = Client(account_sid, auth_token)
            bd = str('\n\nPreço dessa jabirosca chamada SPE tá zerando CUIDA!!\n\nJá tá'+content+'\n\njpfilhooo btw')
            client.messages.create(from_="+17408411652", body=bd, to="+5588988562749")
            print('Mensagem enviada')
            ok = True
            break
        
def recall():
    global ok
    if ok == True:
        _main_()

_main_()
recall()

#print(content)
#print('"{}"'.format(bs.title.string)+" é o nome da tag")
