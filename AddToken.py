# api
import requests
import json

from web3 import Web3

private_key = 'a62b76ffc32ac4c84a6adb47b40b1c9957e5e4221d63b898cd8fa4146d60f6f0'
ankr_url = 'https://apis.ankr.com/c9620180182d471881027a3195a7806f/68be2fdb4a6658325e31f3765ed6c4fc/binance/full/main'

key_bsc = '4QPP4QC7PZSQQCESUQVGIJH5A5MNK5NSVI'

web3 = Web3(Web3.HTTPProvider(ankr_url))

def to_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def get_json(filename):
    with open(filename) as file:
            data = json.load(file)
    return data

def get_abi(contract_address, key):
    data = requests.get('https://api.bscscan.com/api?module=contract&action=getabi&address=' + contract_address + '&apikey=' + key)
    abi = json.loads(data.text)['result']
    return abi

def get_token_info(address):
    abi = get_abi(web3.toChecksumAddress(address), key_bsc)
    contract = web3.eth.contract(address=web3.toChecksumAddress(address), abi=abi)
    name = contract.functions._name().call()
    decimals = contract.functions._decimals().call()
    symbol = contract.functions._symbol().call()
    info = {
        "address": web3.toChecksumAddress(address),
        "name": name,
        "symbol": symbol,
        "decimals": decimals
    }
    return info

def add_token(address):
    info = get_token_info(address)
    with open('Tokens.json') as tokens_json:
        tokens = json.load(tokens_json)
    tokens["tokens"].append(info)
    to_json(tokens, 'Tokens.json')

def get_balance(token_address, wallet_address):
    info = requests.get('https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=' + token_address + '&address=' + wallet_address + '&tag=latest&apikey=' + key_bsc)
    balance = int(json.loads(info.text)['result'])
    balance = web3.fromWei(balance, 'ether')
    return balance
