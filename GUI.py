import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'CodeFiles')

import WebScraping as FP

import tkinter as tk
from tkinter import StringVar, IntVar
import tkinter.ttk as ttk
import pandas as pd
from urllib.request import urlopen
import webbrowser
import functools

dict = {}

labels = []
buttons = []

root = tk.Tk()

"""
This launches the web browser with the URL specified
"""
def search(url):
    #this accounts for when the article is on their own website
    if "/news/stock" in url:
        url = "https://markets.businessinsider.com/" + url
    webbrowser.open(url,new=0)

class CustomWidget(tk.Frame):
    def __init__(self, parent, label, rowNum, company_data):
        tk.Frame.__init__(self, parent)

        self.lb2 = tk.Label(root, text = label, justify='center',font = 'Helvetica 22')
        self.lb2.grid(row=rowNum,columnspan=2,sticky=tk.N+tk.E+tk.W+tk.S)

        self.priceLabel =tk.Label(root,justify="center",font='Helvetica 18',text = "$"+ company_data.price)
        self.priceLabel.grid(row=rowNum +1, column=0,sticky =tk.N+tk.E+tk.W+tk.S)

        self.lb3 = tk.Label(root,justify="center")
        if(company_data.up):
            self.lb3.config(text="▲" + " $" + company_data.change,fg="green")
        else:
            self.lb3.config(text = "▼" + " $" + company_data.change,fg="red")
        self.lb3.grid(row=rowNum+1, column=1, sticky =tk.N+tk.E+tk.W+tk.S)

    def change(self):
        self.lb2.config(text = "Please select the stock from the list below:")
        self.lb3.grid_forget()

    def change2(self, company_data):
        self.lb2.config(text = company_data.name.upper()+" ("+ company_data.stock_ticker.upper()+")",font='Helvetica 18 bold')
        try:
            if company_data.price == "No Price Data":
                self.priceLabel.config(text = company_data.price)
                self.lb3.config(text = company_data.change, fg = "black")
            else:
                self.priceLabel.config(text="$"+ company_data.price)
                if(company_data.up):
                    self.lb3.config(text="▲" + " $" + company_data.change,fg="green")
                else:
                    self.lb3.config(text = "▼" + " $" + company_data.change,fg="red")
        except:
       	    self.priceLabel.config(text="No price data")
            self.lb3.config(text="No price data", fg = "black")
        self.lb3.grid(row=5, column=1)
    def forget(self):
        self.lb2.grid_forget()
        self.lb3.grid_forget()
        self.priceLabel.grid_forget()


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.sv = StringVar()
        self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.callback(sv))

        self.lb1 = tk.Label(root, text='Enter stock ticker:').grid(row=0,columnspan=2)

        self.e1 = tk.Entry(root, textvariable=self.sv)
        self.e1.grid(row=1,columnspan =2)
        self.e1.focus()

        self.cb = tk.Button(root, text = "OK", command=self.change, justify ='center')
        self.cb.grid(row=2,columnspan=2)

        self.DOW, self.SP, self.NASDAQ = FP.frontPageScrape()
        self.details = CustomWidget(self, self.DOW.name, 4,self.DOW)

        self.SPLabel = CustomWidget(self,self.SP.name,6, self.SP)

        self.NASDAQLabel = CustomWidget(self,self.NASDAQ.name,8,self.NASDAQ)

        self.SearchResults = tk.Listbox(width=50)
        #SearchResults.grid(row=6)

        self.newsTitle = tk.Label(root, text="News", font=22)

        self.separator1 = ttk.Separator(root, orient="horizontal")
        self.separator2 = ttk.Separator(root, orient="horizontal")

    """
    Reacts to the callback of the entry box
    Just sets the button state back to normal and clears selection in selection list
    """
    def callback(self,sv):
        self.cb.config(state = "normal")
        self.SearchResults.selection_clear(0, 'end')


    """
    This method is called when the "OK" or enter button are clicked
    """
    def change(self):
        self.SPLabel.forget()
        self.NASDAQLabel.forget()
        try:
            self.words = self.SearchResults.get(self.SearchResults.curselection()).split()
            self.stock_ticker = self.words[-1]
        except:
            self.stock_ticker = self.e1.get()

        self.company_data = FP.searchWebsite(self.stock_ticker)

        for x in range(0,len(labels)):
            labels[x].grid_forget()
            buttons[x].grid_forget()
        labels.clear()
        buttons.clear()

        if isinstance(self.company_data, pd.core.frame.DataFrame):
            self.newsTitle.grid_forget()
            self.separator2.grid_forget()
            self.details.change()
            self.SearchResults.grid(row=5)
            self.SearchResults.delete(0,'end')
            for index, row in self.company_data.iterrows():
                self.SearchResults.insert(index, row['Name'] + " " + row['Symbol'])
        else:
            self.SearchResults.grid_forget()
            self.e1.delete(0,'end')
            self.e1.insert(0,self.stock_ticker)
            #self.name, self.stock_ticker, self.price = self.company_data.getData()
            self.details.change2(self.company_data)
            self.index = 0

            self.newsTitle.grid(row=6, columnspan=2)
            self.separator2.grid(row=7, columnspan=2, sticky="we")

            self.cb.config(state=tk.DISABLED)
            self.indexNum =0
            self.rowNum = 8

            for index, row in self.company_data.news.iterrows():
                dict[row['title']] = row['url']
                labels.append(tk.Label(root, text=row['title'],wraplength=400))
                labels[index].grid(row=self.rowNum, column=self.indexNum,padx=10)
                buttons.append(tk.Button(root,text=row['website']))
                buttons[index].configure(command = functools.partial(search, row['url']))
                buttons[index].grid(row=self.rowNum+1, column=self.indexNum)
                if (self.indexNum % 2) ==1 :
                    self.indexNum = 0
                    self.rowNum +=2
                else:
                    self.indexNum +=1


if __name__ == "__main__":

    root.title('Stock Market')
    # Setting icon of master window
    p1 = tk.PhotoImage(file = 'Images/stock-market-icon-59.png')
    root.iconphoto(False, p1)
    Example(root).place(x=0, y=0, relwidth=1, relheight=1)

    root.mainloop()
