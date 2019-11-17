# EE551FinalProject #
This repository will contain code relevant to my EE551 Engineering Programming: Python class.

## Description ##
For this project I intend on creating a stock quote tracker. This application will allow a user to enter a symbol for a stock that they are curious about the price. The program will return the price possibly within a GUI that will have a green or red arrow depending on if the price is up or down for that day. In addtion, a user will be able to select how often they want to be notified about the stock price. The application will then emit a pop up or message with the stock price for every specified amount of time that the user wants.

## Commits ##
### Add web scraping functionality ###
* Import lxml needs to be installed using `sudo apt-get install python3-lxml`
* Inspect the elements of the webpage using right click -> inspect
* Using arrow in the top left hand corner of inspect
* Click element you need
* Right click the element and copy the full xpath
* Using tree.xpath(‘[path copied]/text()’) and set equal to variable
* Variable will be a list
* Print first element of list

### Add search functionality ###
* Allow user to enter stock ticker
* Generate a URL by adding ‘/[stockTicker]-stock’ to end of https://markets.businessinsider.com/stocks
* Use scraping methods from earlier to get stock prices

### Add webscraping for tables ###
* Allows user to enter name of company
* Shows in table form all stock tickers of companies that are returned
* Uses pandas to format data
* sudo apt-get install python3-pandas
* `displaySearch()` method found mostly from https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059

### Add GUI ###
* Add main.py file
* Going to be used for testing all the methods on the terminal
* Install tkinter `sudo apt-get install python3-tk`
* Add GUI file
* Going to house all of the GUI that will call the methods
* Create basic GUI
* When a button is clicked makes call to `searchWebsite()`
* Changes a label with the data received back from the method

### Add Entry Box ###
* When the button is clicked take data from the entry box
* Display the returned data in the label
* Add Listbox
* If a panadas dataframe is returned we display the data in a listbox rather than in text
- [ ] Want to add the ability to select one item from the list box and click OK to submit

### Clear Listbox on Search ###
* Simply clears the Listbox when a new stock is searched for
