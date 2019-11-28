from lxml import html
import requests
import time
import pandas as pd

"""
A company class contains all the information important to display for a company's stock
"""
class company(object):
    def __init__(self,stock_ticker,name,price,up,change,news):
        self.stock_ticker = stock_ticker
        self.name = name
        self.price = price
        self.up = up
        self.change = change
        self.news = news
    def __str__(self):
        return("The price of {0} ({1}) is ${2}.".format(self.name, self.stock_ticker, self.price))
    def getData(self):
        return(self.name.upper(), self.stock_ticker, self.price)

"""
This method grabs all of the information need from the website
"""
def webScraping(tree):
    up = True
    name = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/h1/span[1]/text()')
    price = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[1]/span/text()')
    image = tree.xpath('//*[@class="icon-set change-indicator-arrow arrow-up-big"]')
    changeNumber = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[2]/span[1]/div[1]/span/text()')
    changePercent = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[2]/span[1]/div[2]/span/text()')
    if len(image) == 0:
        up = False
    news = displayNews(tree)
    return name, price, up, changeNumber, changePercent ,news

"""
This method contains the web scarping for the news tables
"""
def displayNews(tree):
    tr_elements = tree.xpath('//tr')
    if(len(tr_elements)==0):
        return "No Results Found :("
    col=[]
    i=0
    hrefs = tree.xpath('//a[@class="news-link"]')
    titles = tree.xpath('//a[@class="news-link"]')
    websites = tree.xpath('//span[@class="warmGrey source-and-publishdate"]/text()')

    col.append(("title",[]))
    col.append(("url",[]))
    col.append(("website",[]))
    for j in range(0,len(tr_elements)):
        # T is our j'th row
        T=tr_elements[j]

        if len(T)!=1:
            break

        # Iterate through each element of the row
        for t in T.iterchildren():
            # Check if row is empty
            if i>0:
            # Convert any numerical value to integers
                try:
                    data=int(data)
                except:
                    pass
            # Append the titles, url, and websites to correct columns
            col[0][1].append(titles[j].text_content())
            col[1][1].append(hrefs[j].attrib['href'])
            col[2][1].append(websites[j+2])
            websites.pop(j+3)

    Dict={title:column for (title,column) in col}
    df=pd.DataFrame(Dict)

    return df

"""
From this we want to grab all of the results from the table
when a search term is entered. Used this
https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
"""
def displaySearch(tree):
    tr_elements = tree.xpath('//tr')
    if(len(tr_elements)==0):
        return "No Results Found :("
    col=[]
    i=0
    # For each row, store each first element (header) and an empty list
    for t in tr_elements[0]:
        i+=1
        name=t.text_content()
        name=' '.join(name.split())
        col.append((name,[]))

    for j in range(1,len(tr_elements)):
        # T is our j'th row
        T=tr_elements[j]

        # If row is not of size 3, the //tr data is not from our table
        if len(T)!=3:
            break

        # i is the index of our column
        i=0

        # Iterate through each element of the row
        for t in T.iterchildren():
            data=t.text_content()
            data=' '.join(data.split())
            # Check if row is empty
            if i>0:
            # Convert any numerical value to integers
                try:
                    data=int(data)
                except:
                    pass
            # Append the data to the empty list of the i'th column
            col[i][1].append(data)
            # Increment i for the next column
            i+=1

    Dict={title:column for (title,column) in col}
    df=pd.DataFrame(Dict)
    # We only care about the name and Symbol of the stock
    # We also only want the stocks that actually have a symbol
    return df[['Name','Symbol']].loc[df['Symbol'] != '']

"""
This method will actually go out and hit the website
We return a company class, if the website finds the stock ticker
Otherwise it returns a pandas dataframe.
"""
def searchWebsite(searchTerm):
    requestUrl = 'https://markets.businessinsider.com/searchresults?_search='+searchTerm
    page = requests.get(requestUrl)
    tree = html.fromstring(page.text)

    name, price, up, changeNumber, changePercent, news = webScraping(tree)

    # if we get data back from webscarping we return a company object
    if(len(name)!=0 or len(price)!=0):
        try:
            name = name[0].split()
            stock_ticker = name[:-1]
            del name[-1]
            name = ' '.join(name)
            change = changeNumber[0] + " " + changePercent[0]
            return(company(searchTerm, name,price[0],up,change,news))
        except:
            return ("There is no price data on this stock")

    # otherwise we have to display the search terms
    return displaySearch(tree)