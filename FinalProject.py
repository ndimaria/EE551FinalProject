from lxml import html
import requests
import time
import pandas as pd

def webScraping(tree):
    name = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/h1/span[1]/text()')
    price = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[1]/span/text()')
    return name, price
    #if(len(name) == 0 or len(price)==0):
    #    print("I am sorry your stock could not be found")
    #else:
    #    print("The price of {0} is ${1}".format(name[0],price[0]))
    pass

def symbolSearch(symbol):
    requestUrl = 'https://markets.businessinsider.com/stocks/'+symbol+'-stock'
    page = requests.get(requestUrl)

    tree = html.fromstring(page.content)
    name, price = webScraping(tree)
    if(len(name) == 0 or len(price)==0):
        print("I am sorry your stock could not be found")
    else:
        print("The price of {0} is ${1}".format(name[0],price[0]))
    pass

def displaySearch(tree):
    tr_elements = tree.xpath('//tr')
    if(len(tr_elements)==0):
        return "No Results Found :("
    col=[]
    i=0
    #   For each row, store each first element (header) and an empty list
    for t in tr_elements[0]:
        i+=1
        name=t.text_content()
        name=' '.join(name.split())
        col.append((name,[]))

    for j in range(1,len(tr_elements)):
        #T is our j'th row
        T=tr_elements[j]

        #If row is not of size 10, the //tr data is not from our table
        if len(T)!=3:
            break

        #i is the index of our column
        i=0

        #Iterate through each element of the row
        for t in T.iterchildren():
            data=t.text_content()
            data=' '.join(data.split())
            #Check if row is empty
            if i>0:
            #Convert any numerical value to integers
                try:
                    data=int(data)
                except:
                    pass
            #Append the data to the empty list of the i'th column
            col[i][1].append(data)
            #Increment i for the next column
            i+=1

    Dict={title:column for (title,column) in col}
    df=pd.DataFrame(Dict)

    return df[['Name','Symbol']].loc[df['Symbol'] != '']
    pass

def searchWebsite(searchTerm):
    requestUrl = 'https://markets.businessinsider.com/searchresults?_search='+searchTerm
    page = requests.get(requestUrl)
    tree = html.fromstring(page.content)

    name, price = webScraping(tree)

    if(len(name)!=0 or len(price)!=0):
        try:
            print("The price of {0} is ${1}".format(name[0],price[0]),end = '\n\n')
            return
        except:
            print("There is no price data on this stock",end = '\n\n')
            return

    searchData = displaySearch(tree)
    print('')
    print(searchData, end = '\n\n')

while(1):
    #symbol = input("Enter stock ticker to see stock price: ")
    #symbolSearch(symbol)
    searchTerm = input("What stock are you looking for: ")
    searchWebsite(searchTerm)
