from lxml import html
import requests
import time
import pandas as pd

"""
Basic web scraping grabs the name of the stock
as well as the price of the stock from the HTML
"""
def webScraping(tree):
    name = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/h1/span[1]/text()')
    price = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[1]/span/text()')
    return name, price

"""
From this we want to grab all of the results
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
This method will actually goes out and hits the website
"""
def searchWebsite(searchTerm):
    requestUrl = 'https://markets.businessinsider.com/searchresults?_search='+searchTerm
    page = requests.get(requestUrl)
    tree = html.fromstring(page.content)

    name, price = webScraping(tree)

    # if we get data back from webscarping we just display it
    if(len(name)!=0 or len(price)!=0):
        try:
            return ("The price of {0} is ${1}".format(name[0],price[0]))
        except:
            return ("There is no price data on this stock")


    # otherwise we have to display the search terms
    return displaySearch(tree)

def upOrDown(searchTerm):
    up =True
    requestUrl = 'https://markets.businessinsider.com/searchresults?_search='+searchTerm
    page = requests.get(requestUrl)
    tree = html.fromstring(page.content)
    image = tree.xpath('//*[@class="icon-set change-indicator-arrow arrow-up-big"]')

    if len(image) == 0:
        return(not up)
    else:
        return(up)
