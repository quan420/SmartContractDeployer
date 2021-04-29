# api
import requests
import json

# web3
from web3 import Web3

# time
import calendar
import time

# GUI
from tkinter import *

discord_me = 'https://discord.com/api/webhooks/834679729621041182/XJTeEp5OgwCq1eaAcyhXku3hhJCsMLpzzgzS_ePlwHmZjvYGSVlRCHaIgENaj6t1XThU'
discord_stonk = 'https://discord.com/api/webhooks/829961736127512596/BEeH86jp-QMbTBDyLrBWxZnlUOeV-xL6hHM3E7tdC4567rFdiJCPtVCky_WnE6rbiHZj'

key_bsc = '4QPP4QC7PZSQQCESUQVGIJH5A5MNK5NSVI'

my_address = '0x73Ab9BAcf813c4A7c13d5a9F71F693798f0890DB'
other_address = '0x1F32732461d68b9dA205ADAa450E97883D7793dd'

private_key = 'a62b76ffc32ac4c84a6adb47b40b1c9957e5e4221d63b898cd8fa4146d60f6f0'

pancakeswap_router = '0x10ED43C718714eb63d5aA57B78B54704E256024E'

ganache_url = 'http://127.0.0.1:7545/'
ankr_url = 'https://apis.ankr.com/c9620180182d471881027a3195a7806f/68be2fdb4a6658325e31f3765ed6c4fc/binance/full/main'

web3 = Web3(Web3.HTTPProvider(ankr_url))

"""
def to_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def get_abi(contract_address, key):
    data = requests.get('https://api.bscscan.com/api?module=contract&action=getabi&address=' + contract_address + '&apikey=' + key)
    abi = json.loads(data.text)['result']
    return abi

def write_contract(amountIn, amountOutMin, path, to, deadline):
    tx_hash = contract.functions.swapExactTokensForTokens(
        amountIn=amountIn,
        amountOutMin=amountOutMin,
        path=path,
        to=to,
        deadline=deadline
    )
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print(tx_receipt)

abi = get_abi(pancakeswap_router, key_bsc)

contract = web3.eth.contract(address=pancakeswap_router, abi=abi)

ts = calendar.timegm(time.gmtime())
print(ts)
"""

window = Tk()

window.geometry('800x600')

window.title('PancakeSwap Swapper')

sell_token = Entry(window, width = 50)
sell_token.grid(column=1, row=0)

window.mainloop()

if __name__ == '__main__':
    print('Press Ctrl-C / Ctrl-Q to stop.')




