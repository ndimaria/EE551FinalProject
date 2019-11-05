import tkinter as tk
import FinalProject as FP
from tkinter import StringVar, IntVar

root = tk.Tk()
root.title('Stock Market')
def change():
    stock_ticker = e1.get()
    lb2.config(text = FP.searchWebsite(stock_ticker))

lb1 = tk.Label(root, text='Enter stock ticker:',width = 50)
lb1.pack()
e1 = tk.Entry(root)
e1.pack()

cb = tk.Button(root, text = "OK", command=change, justify ='center')
cb.pack()

lb2 = tk.Label(root, text = "Stock data will display here.", justify='center',width = 50)
lb2.pack()

root.mainloop()
