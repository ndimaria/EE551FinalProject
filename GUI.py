import tkinter as tk
import FinalProject as FP
from tkinter import StringVar, IntVar
import pandas as pd
from urllib.request import urlopen
import webbrowser
import functools

root = tk.Tk()
root.title('Stock Market')
dict = {}

labels = []
buttons = []

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
    for x in range(0,len(labels)):
        labels[x].grid_forget()
        buttons[x].grid_forget()
    labels.clear()
    buttons.clear()
    if isinstance(company_data, pd.core.frame.DataFrame):
        lb2.config(text = "Please select the stock from the list below:")
        lb3.config(text = "Click okay button when stock selected", fg = "black")
        SearchResults.grid(row=5)
        SearchResults.delete(0,'end')
        for index, row in company_data.iterrows():
            SearchResults.insert(index, row['Name'] + " " + row['Symbol'])
    else:
        SearchResults.grid_forget()
        e1.delete(0,'end')
        e1.insert(0,stock_ticker)
        lb2.config(text = company_data.getData())

        if(company_data.up):
            lb3.config(text="▲"+company_data.change,fg="green")
        else:
            lb3.config(text = "▼"+ company_data.change,fg="red")
        index = 0

        cb.config(state=tk.DISABLED)
        indexNum =0
        rowNum = 5

        for index, row in company_data.news.iterrows():
            dict[row['title']] = row['url']
            labels.append(tk.Message(root, text=row['title']))
            labels[index].grid(row=rowNum, column=indexNum)
            buttons.append(tk.Button(root,text=row['website']))
            buttons[index].configure(command = functools.partial(search, row['url']))
            buttons[index].grid(row=rowNum+1, column=indexNum)
            if (indexNum % 2) ==1 :
                indexNum = 0
                rowNum +=2
            else:
                indexNum +=1

def func(event):
    change()
root.bind('<Return>', func)

def search(url):
    #this accounts for when the article is on their own website
    if "/news/stock" in url:
        url = "https://markets.businessinsider.com/" + url
    webbrowser.open(url,new=0)

def callback(sv):
    cb.config(state="normal")
    SearchResults.selection_clear(0, 'end')

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

lb1 = tk.Label(root, text='Enter stock ticker:').grid(row=0,columnspan=2)

e1 = tk.Entry(root, textvariable=sv)
e1.grid(row=1,columnspan =2)
e1.focus()

cb = tk.Button(root, text = "OK", command=change, justify ='center')
cb.grid(row=2,columnspan=2)

lb2 = tk.Label(root, text = "Stock data will display here.", justify='center')
lb2.grid(row=3,columnspan=2)

lb3 = tk.Label(root)
lb3.grid(row=4,columnspan=2)

SearchResults = tk.Listbox(width=50)
SearchResults.grid(row=5)

root.mainloop()
