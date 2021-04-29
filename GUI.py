from tkinter import *
from tkinter.ttk import *
import json

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


window = Tk()
window.title('PancakeSwap Swapper')

sell_token_address = StringVar()
sell_tokens = Combobox(window, textvariable=sell_token_address)
sell_tokens['values'] = get_symbols()
sell_tokens.grid(column=0, row=1, columnspan=2, ipadx=300)

buy_token_address = StringVar()
buy_tokens = Combobox(window, textvariable=buy_token_address)
buy_tokens['values'] = get_symbols()
buy_tokens.grid(column=0, row=0, columnspan=2, ipadx=300)

swap = Button(window, text='Swap')
swap.grid(column=0, row=2)

add_token = Button(window, text='Add Token')
add_token.grid(column=1, row=2)

sell_orders_listbox = Listbox(window)
sell_orders_listbox.grid(column=0, row=3, ipadx=100, pady=20)

sell_orders_listbox = Listbox(window)
sell_orders_listbox.grid(column=1, row=3, ipadx=100, pady=20)

window.mainloop()


        
    
        
