import tkinter as tk
import FinalProject as FP
from tkinter import StringVar, IntVar
import pandas as pd

root = tk.Tk()
root.title('Stock Market')
def change():
    stock_ticker = e1.get()
    data = FP.searchWebsite(stock_ticker)

    if isinstance(data, pd.core.frame.DataFrame):
        Lb = tk.Listbox()
        for index, row in data.iterrows():
            Lb.insert(index, row['Name'] + " " + row['Symbol'])
            print(row['Name'], row['Symbol'])
        Lb.pack()
    else:
        lb2.config(text = data)
"""
def func(event):
    stock_ticker = e1.get()
    lb2.config(text = FP.searchWebsite(stock_ticker))
root.bind('<Return>', func)
"""

lb1 = tk.Label(root, text='Enter stock ticker:',width = 50)
lb1.pack()
e1 = tk.Entry(root)
e1.pack()

cb = tk.Button(root, text = "OK", command=change, justify ='center')
cb.pack()

lb2 = tk.Label(root, text = "Stock data will display here.", justify='center',width = 50)
lb2.pack()

root.mainloop()
