import tkinter as tk
import FinalProject as FP
from tkinter import StringVar, IntVar
import pandas as pd

root = tk.Tk()
root.title('Stock Market')
def change():
    try:
        words = Lb.get(Lb.curselection()).split()
        stock_ticker = words[-1]

    except:
        stock_ticker = e1.get()

    data = FP.searchWebsite(stock_ticker)
    up = FP.upOrDown(stock_ticker)

    if isinstance(data, pd.core.frame.DataFrame):
        Lb.delete(0,'end')
        for index, row in data.iterrows():
            Lb.insert(index, row['Name'] + " " + row['Symbol'])
    else:
        Lb.delete(0,'end')
        e1.delete(0,'end')
        e1.insert(0,stock_ticker)
        lb2.config(text = data)
        if(up):
            image.config(image=upArrow)
        else:
            image.config(image=downArrow)

def func(event):
    change()
root.bind('<Return>', func)

lb1 = tk.Label(root, text='Enter stock ticker:',width = 50)
lb1.pack()
e1 = tk.Entry(root)
e1.pack()
e1.focus()

cb = tk.Button(root, text = "OK", command=change, justify ='center')
cb.pack()

lb2 = tk.Label(root, text = "Stock data will display here.", justify='center',width = 50)
lb2.pack()

upArrow = tk.PhotoImage(file="UpArrow.pgm")
downArrow = tk.PhotoImage(file="DownArrow.pgm")
image = tk.Label(root)
image.pack()

Lb = tk.Listbox(width =50)
Lb.pack()


root.mainloop()
