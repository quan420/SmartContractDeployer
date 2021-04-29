import json

def to_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def add_buy_order():
    try:
        with open('Buy_Orders.json') as buy_orders_json:
            buy_orders = json.load(buy_orders_json)
    except Exception:
        buy_orders = {
            "orders": []
        }

    price = input('Price: ')
    amount = input('Amount: ')
    order = {
        'price': price, 
        'amount': amount
        }
    print(order)
    buy_orders["orders"].append(order)
    print(buy_orders)

    to_json(buy_orders, 'Buy_Orders.json')

    print('Buy Order Added')

if __name__ == '__main__':
    print('Press Ctrl-C / Ctrl-Q to stop.')
    add_buy_order()
    quit()

    
    