import json

def to_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def remove_sell_order(index):
    with open('Sell_Orders.json') as sell_orders_json:
        sell_orders = json.load(sell_orders_json)

    sell_orders['orders'].pop(index)

    to_json(sell_orders, 'Sell_Orders.json')

    print('Order Removed')

if __name__ == '__main__':
    print('Press Ctrl-C / Ctrl-Q to stop.')
    index = int(input('Sell Order ID: '))
    remove_sell_order(index)
    quit()

    
    