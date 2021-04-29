from tkinter import *
from tkinter.ttk import *
import json
import AddToken

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

def add_new_token():
    add_token_window = Tk()
    add_token_window.title('Add Token')
    add_token_input = Entry(add_token_window)
    add_token_input.grid(column=0, row=0, ipadx=150)
    add_token_button = Button(add_token_window, text='Add', command= lambda: AddToken.add_token(add_token_input.get()))
    add_token_button.grid(column=1, row=0)
    add_token_window.mainloop

window = Tk()
window.title('PancakeSwap Swapper')

sell_token_address = StringVar()
sell_tokens = Combobox(window, textvariable=sell_token_address)
sell_tokens['values'] = get_symbols()
sell_tokens.grid(column=0, row=1, ipadx=300)

buy_token_address = StringVar()
buy_tokens = Combobox(window, textvariable=buy_token_address)
buy_tokens['values'] = get_symbols()
buy_tokens.grid(column=0, row=0, ipadx=300)

swap = Button(window, text='Swap')
swap.grid(column=0, row=2)

add_token_button = Button(window, text='Add Token', command= lambda: add_new_token())
add_token_button.grid(column=1, row=2)

sell_orders_listbox = Listbox(window)
sell_orders_listbox.grid(column=0, row=3, ipadx=100, pady=20)

sell_orders_listbox = Listbox(window)
sell_orders_listbox.grid(column=1, row=3, ipadx=100, pady=20)

balance_label = Label(text=) 

window.mainloop()


        
    
        
