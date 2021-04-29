# api
import requests
import json

from web3 import Web3

private_key = 'a62b76ffc32ac4c84a6adb47b40b1c9957e5e4221d63b898cd8fa4146d60f6f0'
ankr_url = 'https://apis.ankr.com/c9620180182d471881027a3195a7806f/68be2fdb4a6658325e31f3765ed6c4fc/binance/full/main'

print(1)
web3 = Web3(Web3.HTTPProvider(ankr_url))

print(web3.isConnected)

def get_token_info(address):
    info = web3.eth.contract(address).functions._name.call()
    print(info)

get_token_info('0x55d398326f99059ff775485246999027b3197955')