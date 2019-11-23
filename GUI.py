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

    company_data = FP.searchWebsite(stock_ticker)

    if isinstance(company_data, pd.core.frame.DataFrame):
        Lb.delete(0,'end')
        for index, row in company_data.iterrows():
            Lb.insert(index, row['Name'] + " " + row['Symbol'])
    else:
        Lb.delete(0,'end')
        e1.delete(0,'end')
        e1.insert(0,stock_ticker)
        lb2.config(text = company_data.getData())

        if(company_data.up):
            lb3.config(text="▲"+company_data.change,fg="green")
        else:
            lb3.config(text = "▼"+ company_data.change,fg="red")
        index = 0
        for index, row in company_data.news.iterrows():
            Lb.insert(index,row['title'])
            index+=1

def func(event):
    change()
root.bind('<Return>', func)

lb1 = tk.Label(root, text='Enter stock ticker:').grid(row=0)

e1 = tk.Entry(root)
e1.grid(row=1)
e1.focus()

cb = tk.Button(root, text = "OK", command=change, justify ='center')
cb.grid(row=2)

lb2 = tk.Label(root, text = "Stock data will display here.", justify='center')
lb2.grid(row=3)

lb3 = tk.Label(root)
lb3.grid(row=4)

Lb = tk.Listbox(width=50)
Lb.grid(row=5)

root.mainloop()
