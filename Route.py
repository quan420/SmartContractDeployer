# api
import requests
import json

# web3
from web3 import Web3

ankr_url = 'https://apis.ankr.com/8a2c4aebebb2478194f40cc3626362ea/68be2fdb4a6658325e31f3765ed6c4fc/binance/full/main'

key_bsc = '4QPP4QC7PZSQQCESUQVGIJH5A5MNK5NSVI'

factory_address = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
factory_abi = '[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[],"name":"INIT_CODE_PAIR_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

WBNB_address = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
BUSD_address = '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56'

IL = 'Insufficient Liquidity'
SIL = 'Sell Insufficient Liquidity'
BIL = 'Buy Insufficient Liquidity'

web3 = Web3(Web3.HTTPProvider(ankr_url))

factory_contract = web3.eth.contract(address=factory_address, abi=factory_abi)

def get_impact_amount(token_address_a, token_address_b, token_amount_a):
    token_index_a = 0
    token_index_b = 1 
    LP_address = factory_contract.functions.getPair(token_address_a, token_address_b).call()
    LP_abi = json.loads(requests.get('https://api.bscscan.com/api?module=contract&action=getabi&address=' + LP_address + '&apikey=' + key_bsc).text)['result']
    LP_contract = web3.eth.contract(address=LP_address, abi=LP_abi)
    LP_reserves = LP_contract.functions.getReserves().call()
    if (token_address_a != LP_contract.functions.token0().call()):
        token_index_a = 1
        token_index_b = 0   
    token_reserve_a = web3.fromWei(LP_reserves[token_index_a], 'ether')
    token_reserve_b = web3.fromWei(LP_reserves[token_index_b], 'ether')
    LP_contantProduct = token_reserve_a * token_reserve_b
    token_price_a = token_reserve_a / token_reserve_b
    if (token_reserve_a > token_amount_a):
        impact = 1 - ((LP_contantProduct / (token_reserve_a + token_price_a * token_amount_a)) / token_reserve_b)
        amount = (token_amount_a / token_price_a) * (1 - impact) 
        return impact, amount
    else:
        return IL

def get_token_route(route, sell_token_amount):
    amount = sell_token_amount
    total_impact = 0
    for x in range(len(route)):
        impact = get_impact_amount(route[x], route[x+1], amount)
        if impact != IL:
            amount = impact[1]
            total_impact = (1 - total_impact) * (1 - impact[0])
        elif impact == IL:
            return IL
    return impact, amount

def get_route(sell_token, buy_token, sell_token_amount):
    route_WBNB = get_token_route([sell_token, WBNB_address, buy_token], sell_token_amount)
    route_BUSD = get_token_route([sell_token, BUSD_address, buy_token], sell_token_amount)
    route_WBNB_BUSD = get_token_route([sell_token, WBNB_address, BUSD_address, buy_token], sell_token_amount)
    route_BUSD_WBNB = get_token_route([sell_token, BUSD_address, WBNB_address, buy_token], sell_token_amount)
    print(route_WBNB)
    print(route_BUSD)
    print(route_WBNB_BUSD)
    print(route_BUSD_WBNB)

get_route(web3.toChecksumAddress('0x55d398326f99059ff775485246999027b3197955'), web3.toChecksumAddress('0x9617857e191354dbea0b714d78bc59e57c411087'), 1000)




