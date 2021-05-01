# Webook
from logging import exception
from dhooks import Webhook, File, Embed

# api
import requests
import json

# dates module
from itertools import count
import time

# spreadsheet
import xlwings as xw

# initiate spreadsheet
wb = xw.Book()
ws = wb.sheets('Sheet1')

# BSCScan key
key = '5U9YWYDVK31UMA18BR4YIRK6HPJMPFW5MJ'

# discord webhooks
discord_stonk = 'https://discord.com/api/webhooks/812236191461146645/3vpQ7oGbvaIEFL65vy4Zx09Au6WceE1YnBjXapA8nwJogLXCGJyzgOLce49lj4HWnwnr'

# liquitity addresses
address_TOKEN_WBNB = '0x718d3BaA161e1A38758bb0f1Fe751E401f431ac4'
address_BUSD_WBNB = '0x1B96B92314C44b159149f7E0303511fB2Fc4774f'

# token addresses
TOKEN_address = '0x5621b5a3f4a8008c4ccdd1b942b121c8b1944f1f'
WBNB_address = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
BUSD_address = '0xe9e7cea3dedca5984780bafc599bd69add087d56'

data_set = {'Token':''}

def to_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def get_token_balance(contract_address, address, token):
    balance = requests.get('https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=' + contract_address + '&address=' + address + '&tag=latest&apikey=' + key)
    balance_json = json.loads(balance.text)
    to_json(balance_json, token + '_Balance.json')
    return balance_json

if __name__ == '__main__':
    print('Press Ctrl-C / Ctrl-Q to stop.')
    while True:
        try:
            for i in count():

                TOKEN_balance = get_token_balance(TOKEN_address, address_TOKEN_WBNB, 'TOKEN')['result']
                TOKEN_balance_length = len(TOKEN_balance)
                TOKEN_balance = TOKEN_balance[:TOKEN_balance_length - 18] + '.' + TOKEN_balance[TOKEN_balance_length - 18:]
                TOKEN_balance = float(TOKEN_balance)

                WBNB_balance = get_token_balance(WBNB_address, address_TOKEN_WBNB,'WBNB')['result']
                WBNB_balance_length = len(WBNB_balance)
                WBNB_balance = WBNB_balance[:WBNB_balance_length - 18] + '.' + WBNB_balance[WBNB_balance_length - 18:]
                WBNB_balance = float(WBNB_balance)

                price_TOKEN_WBNB = WBNB_balance / TOKEN_balance
                price_WBNB_TOKEN = 1 / price_TOKEN_WBNB

                BUSD_balance = get_token_balance(BUSD_address, address_BUSD_WBNB,'BUSD')['result']
                BUSD_balance_length = len(BUSD_balance)
                BUSD_balance = BUSD_balance[:BUSD_balance_length - 18] + '.' + BUSD_balance[BUSD_balance_length - 18:]
                BUSD_balance = float(BUSD_balance)

                WBNB_balance = get_token_balance(WBNB_address, address_BUSD_WBNB,'WBNB')['result']
                WBNB_balance_length = len(WBNB_balance)
                WBNB_balance = WBNB_balance[:WBNB_balance_length - 18] + '.' + WBNB_balance[WBNB_balance_length - 18:]
                WBNB_balance = float(WBNB_balance)

                price_WBNB_BUSD = BUSD_balance / WBNB_balance
                price_BUSD_WBNB = 1/ price_WBNB_BUSD
                price_TOKEN_BUSD =  price_TOKEN_WBNB * price_WBNB_BUSD
                price = price_TOKEN_BUSD

                ws.range('A1').value = 'TOKEN/BUSD'
                ws.range('B1').value = 'TOKEN/WBNB'
                ws.range('C1').value = 'WBNB/TOKEN'
                ws.range('D1').value = 'WBNB/BUSD'

                ws['A1'].font.bold = True
                ws['B1'].font.bold = True
                ws['C1'].font.bold = True
                ws['D1'].font.bold = True

                ws.range('A2').value = price_TOKEN_BUSD
                ws.range('B2').value = price_TOKEN_WBNB
                ws.range('C2').value = price_WBNB_TOKEN
                ws.range('D2').value = price_WBNB_BUSD

                data_set['Token'] = str(price_TOKEN_BUSD)
                to_json(data_set, 'Price.json')

                wb.save('PriceSheet.xlsx')

                print(f'Iteration {i}')
        except Exception:
            continue

