from lxml import html
import requests
import time

def webScraping(tree):
    name = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/h1/span[1]/text()')
    price = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[1]/span/text()')
    if(len(name) == 0 or len(price)==0):
        print("I am sorry your stock could not be found")
    else:
        print("The price of {0} is ${1}".format(name[0],price[0]))
    pass

def searchWebsite(symbol):
    requestUrl = 'https://markets.businessinsider.com/stocks/'+symbol+'-stock'
    page = requests.get(requestUrl)

    tree = html.fromstring(page.content)
    webScraping(tree)
    pass

while(1):
    symbol = input("Enter stock ticker to see stock price: ")
    searchWebsite(symbol)
