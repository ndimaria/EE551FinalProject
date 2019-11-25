import tkinter as tk
import FinalProject as FP
from tkinter import StringVar, IntVar
import pandas as pd
from urllib.request import urlopen
import webbrowser

root = tk.Tk()
root.title('Stock Market')
dict = {}

global news
news = False

p1 = tk.PhotoImage(file = 'stock-market-icon-59.png')

# Setting icon of master window
root.iconphoto(False, p1)

def change():

    try:
        words = SearchResults.get(SearchResults.curselection()).split()
        stock_ticker = words[-1]
    except:
        stock_ticker = e1.get()

    company_data = FP.searchWebsite(stock_ticker)

    if isinstance(company_data, pd.core.frame.DataFrame):
        lb2.config(text = "Please select the stock from the list below:")
        lb3.config(text = "Click okay button when stock selected", fg = "black")
        cb1.config(state= tk.DISABLED)
        NewsResults.grid_forget()
        SearchResults.grid(row=5)
        SearchResults.delete(0,'end')
        for index, row in company_data.iterrows():
            SearchResults.insert(index, row['Name'] + " " + row['Symbol'])
    else:
        NewsResults.delete(0,'end')
        SearchResults.grid_forget()
        NewsResults.grid(row=5)
        e1.delete(0,'end')
        e1.insert(0,stock_ticker)
        lb2.config(text = company_data.getData())
        global news
        news = True
        
        if(company_data.up):
            lb3.config(text="▲"+company_data.change,fg="green")
        else:
            lb3.config(text = "▼"+ company_data.change,fg="red")
        index = 0

        cb.config(state=tk.DISABLED)
        cb1.config(state="normal")
        for index, row in company_data.news.iterrows():
            dict[row['title']] = row['url']
            NewsResults.insert(index,row['title'])
            index+=1

def func(event):
    global news
    if(not news):
        change()
    else:
        search()
root.bind('<Return>', func)

def search():
    url = dict[NewsResults.get(NewsResults.curselection())]
    #this accounts for when the article is on their own website
    if "/news/stock" in url:
        url = "https://markets.businessinsider.com/" + url
    webbrowser.open(url,new=0)

def callback(sv):
    cb.config(state="normal")
    SearchResults.selection_clear(0, 'end')
    NewsResults.selection_clear(0, 'end')

    global news
    news = False

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

lb1 = tk.Label(root, text='Enter stock ticker:').grid(row=0)

e1 = tk.Entry(root, textvariable=sv)
e1.grid(row=1)
e1.focus()

cb = tk.Button(root, text = "OK", command=change, justify ='center')
cb.grid(row=2)

lb2 = tk.Label(root, text = "Stock data will display here.", justify='center')
lb2.grid(row=3)

lb3 = tk.Label(root)
lb3.grid(row=4)

SearchResults = tk.Listbox(width=50)
SearchResults.grid(row=5)

NewsResults = tk.Listbox(width=50)
NewsResults.grid(row=5)

cb1 = tk.Button(root,text = "Search", command = search, justify='right',state=tk.DISABLED)
cb1.grid(row=6)

root.mainloop()
