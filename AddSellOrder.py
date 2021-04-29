import json

def to_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def add_sell_order():
    try:
        with open('Sell_Orders.json') as sell_orders_json:
            sell_orders = json.load(sell_orders_json)
    except Exception:
        sell_orders = {
            "orders": []
        }

    price = input('Price: ')
    amount = input('Amount: ')
    order = {
        'price': price, 
        'amount': amount
        }
    print(order)
    sell_orders["orders"].append(order)
    print(sell_orders)

    to_json(sell_orders, 'Sell_Orders.json')

    print('Sell Order Added')

if __name__ == '__main__':
    print('Press Ctrl-C / Ctrl-Q to stop.')
    add_sell_order()
    quit()

    
    