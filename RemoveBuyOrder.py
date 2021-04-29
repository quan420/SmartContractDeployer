import json

def to_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def remove_buy_order(index):
    with open('Buy_Orders.json') as buy_orders_json:
        buy_orders = json.load(buy_orders_json)

    buy_orders['orders'].pop(index)

    to_json(buy_orders, 'Buy_Orders.json')

    print('Order Removed')

if __name__ == '__main__':
    print('Press Ctrl-C / Ctrl-Q to stop.')
    index = int(input('Buy Order ID: '))
    remove_buy_order(index)
    quit()

    
    