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

def get_sell_token_balance(event):
    symbol = sell_tokens.get()
    data = get_json('Tokens.json')
    tokens = data['tokens']
    address = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
    for token in tokens:
        if token['symbol'] == symbol:
            address = token['address']
    sell_balance = AddToken.get_balance(address, wallet)
    balance_string = str(round(sell_balance, 2))
    sell_balance_labal_text.set('Balance: ' + balance_string)

def get_buy_token_balance(event):
    symbol = buy_tokens.get()
    data = get_json('Tokens.json')
    tokens = data['tokens']
    address = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
    for token in tokens:
        if token['symbol'] == symbol:
            address = token['address']
    buy_balance = AddToken.get_balance(address, wallet)
    balance_string = str(round(buy_balance, 2))
    buy_balance_labal_text.set('Balance: ' + balance_string)

def get_max():
    sell_token_amount_text.set(str(sell_balance))
    print(sell_balance)

# Main Window
window = Tk()
window.title('PancakeSwap Swapper')

# Sell Amount
sell_token_amount_text = StringVar()
sell_token_amount = Entry(window, textvariable=sell_token_amount_text)
sell_token_amount.grid(column=0, row=0, ipadx=95, ipady=12, sticky=W)

# Sell Token
sell_tokens = Combobox(window)
sell_tokens['values'] = get_symbols()
sell_tokens.current(0)
sell_tokens.grid(column=1, row=0, ipadx=88, sticky=SW)
sell_tokens.bind("<<ComboboxSelected>>", get_sell_token_balance)

# Sell Token Balance
sell_balance_labal_text = StringVar()
sell_balance_labal_text.set('Balance: ' + str(round(sell_balance, 2)))
sell_balance_label = Label(textvariable=sell_balance_labal_text)
sell_balance_label.grid(column=1, row=0, ipady=2, sticky=NW)

# Max Button
max_button = Button(window, text='MAX', command= lambda: get_max())
max_button.grid(column=1, row=0, sticky=NE)

# Buy Amount
buy_token_amount_text = StringVar()
buy_token_amount = Entry(window, textvariable=sell_token_amount_text)
buy_token_amount.grid(column=0, row=1, ipadx=95, ipady=12, sticky=W)

# Buy Token
buy_tokens = Combobox(window)
buy_tokens['values'] = get_symbols()
buy_tokens.current(0)
buy_tokens.grid(column=1, row=1, ipadx=88, sticky=SW)
buy_tokens.bind("<<ComboboxSelected>>", get_buy_token_balance)

# Buy Token Balance
buy_balance_labal_text = StringVar()
buy_balance_labal_text.set('Balance: ' + str(round(buy_balance, 2)))
buy_balance_label = Label(textvariable=buy_balance_labal_text)
buy_balance_label.grid(column=1, row=1, ipady=2, sticky=NW)

# Swap Button
swap = Button(window, text='Swap')
swap.grid(column=0, row=2)

# Add Token Button
add_token_button = Button(window, text='Add Token', command= lambda: add_new_token())
add_token_button.grid(column=1, row=2)

# Buy orders Listbox
buy_orders_listbox = Listbox(window)
buy_orders_listbox.grid(column=0, row=3, ipadx=100, ipady=20, pady=10, sticky=E)

# Sell Order Listbox
sell_orders_listbox = Listbox(window)
sell_orders_listbox.grid(column=1, row=3, ipadx=100, ipady=20, pady=10, sticky=W)

window.mainloop()






        


        
    
        
