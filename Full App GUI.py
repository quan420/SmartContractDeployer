from tkinter import *
from tkinter.ttk import *
import json
import AddToken

wallet = '0x067a6098217cFca37638c7f180fE0e0e9B0177A2'
sell_balance = 0
buy_balance = 0

def get_json(filename):
    with open(filename) as file:
            data = json.load(file)
    return data

def get_symbols():
    tokens = get_json('Tokens.json')
    tokens = tokens['tokens']
    symbols = []
    for token in tokens:
        symbols.append(token['symbol'])
    return symbols

def get_sell_orders():
    sell_orders = get_json('Sell_Orders.json')
    orders = sell_orders['orders']
    return orders

def get_buy_orders():
    buy_orders = get_json('Buy_Orders.json')
    orders = buy_orders['orders']
    return orders

def add_new_token_update(token):
    AddToken.add_token(token)
    buy_tokens['values'] = get_symbols()
    sell_tokens['values'] = get_symbols()

def add_new_token():
    add_token_window = Tk()
    add_token_window.title('Add Token')
    add_token_input = Entry(add_token_window)
    add_token_input.grid(column=0, row=0, ipadx=150)
    add_token_button = Button(add_token_window, text='Add', command=lambda: add_new_token_update(add_token_input.get()))
    add_token_button.grid(column=1, row=0)  
    add_token_window.mainloop

def get_token_balance(symbol):
    data = get_json('Tokens.json')
    tokens = data['tokens']
    for token in tokens:
        if token['symbol'] == symbol:
            address = token['address']
    balance = AddToken.get_balance(address, wallet)
    return balance

def set_sell_token_balance(event):
    symbol = sell_tokens.get()
    balance = get_token_balance(symbol)
    balance_string = str(round(balance, 2))
    sell_balance_labal_text.set('Balance: ' + balance_string)

def set_buy_token_balance(event):
    symbol = buy_tokens.get()
    balance = get_token_balance(symbol)
    balance_string = str(round(balance, 2))
    buy_balance_labal_text.set('Balance: ' + balance_string)

def set_max():
    symbol = sell_tokens.get()
    balance = get_token_balance(symbol)
    balance_string = str(balance)
    sell_token_amount_text.set(str(balance_string))

def add_order():
    sell_token = sell_tokens.get()
    buy_token = buy_tokens.get()
    amount = sell_token_amount.get()
    
# Main Window
window = Tk()
window.title('PancakeSwap Swapper')

# Order Type
v = IntVar()
v.set(2)
limit_order_button = Radiobutton(window, text='Limit Order', variable=v, value=1)
limit_order_button.grid(column=0, row=0, sticky=E)
market_order_button = Radiobutton(window, text='Market Order', variable=v, value=2)
market_order_button.grid(column=0, row=0, sticky=W)

# Sell Amount
sell_token_amount_text = StringVar()
sell_token_amount = Entry(window, textvariable=sell_token_amount_text)
sell_token_amount.grid(column=0, row=1, ipadx=100, ipady=12.5, sticky=W)

# Sell Token
sell_tokens = Combobox(window)
sell_tokens['values'] = get_symbols()
sell_tokens.current(0)
sell_tokens.grid(column=1, row=1, ipadx=90, sticky=SW)
sell_tokens.bind("<<ComboboxSelected>>", set_sell_token_balance)

# Sell Token Balance
sell_balance_labal_text = StringVar()
sell_balance_labal_text.set('Balance: ' + str(round(sell_balance, 2)))
sell_balance_label = Label(textvariable=sell_balance_labal_text)
sell_balance_label.grid(column=1, row=1, ipady=2, sticky=NW)

# Max Button
max_button = Button(window, text='MAX', command= lambda: set_max())
max_button.grid(column=1, row=1, sticky=NE)

# Buy Amount
buy_token_amount_text = StringVar()
buy_token_amount = Entry(window, textvariable=buy_token_amount_text)
buy_token_amount.grid(column=0, row=2, ipadx=100, ipady=12, sticky=W)

# Buy Token
buy_tokens = Combobox(window)
buy_tokens['values'] = get_symbols()
buy_tokens.current(0)
buy_tokens.grid(column=1, row=2, ipadx=90, sticky=SW)
buy_tokens.bind("<<ComboboxSelected>>", set_buy_token_balance)

# Buy Token Balance
buy_balance_labal_text = StringVar()
buy_balance_labal_text.set('Balance: ' + str(round(buy_balance, 2)))
buy_balance_label = Label(textvariable=buy_balance_labal_text)
buy_balance_label.grid(column=1, row=2, ipady=2, sticky=NW)

# Swap Button
swap_button = Button(window, text='Swap')
swap_button.grid(column=0, row=3, sticky=W)

# Add Order Button
add_order_button = Button(window, text='Add Order', command= lambda: add_order())
add_order_button.grid(column=0, row=3, sticky=E)

# Add Token Button
add_token_button = Button(window, text='Add Token', command= lambda: add_new_token())
add_token_button.grid(column=1, row=3)

# Buy orders Listbox
buy_orders_label = Label(window, text='Buy Orders')
buy_orders_label.grid(column=0, row=4, pady=10, sticky=S)

buy_orders_listbox = Listbox(window)
buy_orders = get_buy_orders()
for x in range(len(buy_orders)):
    buy_orders_listbox.insert(x+1, buy_orders[x])
buy_orders_listbox.grid(column=0, row=5, ipadx=100, sticky=NE)

# Sell Order Listbox
sell_orders_label = Label(window, text='Sell Orders')
sell_orders_label.grid(column=1, row=4, pady=10, sticky=S)

sell_orders_listbox = Listbox(window)
sell_orders = get_sell_orders()
for x in range(len(sell_orders)):
    sell_orders_listbox.insert(x+1, sell_orders[x])
sell_orders_listbox.grid(column=1, row=5, ipadx=100, sticky=NW)

window.mainloop()






        


        
    
        
