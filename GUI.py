from tkinter import *
from tkinter.ttk import *

window = Tk()

window.geometry('800x600')

window.title('PancakeSwap Swapper')


buy_tokens = Combobox(window)
buy_tokens['values'] = ('BNB', 'BUSD', 'USDT')
buy_tokens.current(0)
buy_tokens.grid(column=0, row=0, ipadx=200)

sell_tokens = Combobox(window)
sell_tokens['values'] = ('BNB', 'BUSD', 'USDT')
sell_tokens.current(1)
sell_tokens.grid(column=0, row=1, ipadx=200)

window.mainloop()
