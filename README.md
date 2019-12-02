# EE551FinalProject #
This repository will contain code relevant to Nicholas DiMaria's EE551 Engineering Programming: Python final project.

## Description ##
For this project I created a stock quote tracker. This application will allow a user to enter a symbol, or the name of a company that they are curious about the stock price. The program scrapes https://markets.businessinsider.com for all the information. If a stock ticker is entered, the programs displays the price, how much the price has changed (both percent and dollar amount), as well as the news. The news is displayed with a button below each news header to go to that website. If a company name is entered the search results for that company name are returned in a listbox. The correct company can then be selected from the listbox. 

## How to install ##
To download this application just clone this repository. Then install the following:
* `sudo apt-get install python3-lxml`
* `sudo apt-get install python3-pandas`
* `sudo apt-get install python3-tk`

## How to run application ##
### GUI application ###
In the main folder just run `python3 GUI.py`
![GUI Picture](/Images/GUI.png)

### Non-GUI application ###
In the main folder just run `python3 main.py`
![Non-GUI Picture](/Images/NonGUI.png)

## How to use application ##
With the programming running perform the following steps:
* Type the stock ticker or company name in the entry box
* Click the "OK" button or hit enter

If entered a stock ticker:
* Click the button below the news article you are interested in 
  * This will open a browser tab to the news article 
  
If entered a company name:
* Select the company you would like from the listbox
* Click "OK" button or enter again 

## Testing ##
### Description ###
There is a test file that contains two tests. These tests ensure the following:
1. Valid data is returned when passing a stock ticker (specifically "AAPL")
    1. Checks the company stock ticker returned is "AAPL"
    2. Checks the company name is "Apple"
    3. Checks that the price of the stock is greater than 0 
    4. Checks that the company news is a pandas dataframe
    5. Checks that the "change" price in percent and dollars is something similar to "200.00 (1.10%)"
2. A pandas dataframe is returned when a company name is passed (specifically "Apple")

### How to Run ###
* cd to "Tests" folder
* run `python3 -m pytest tests.py`

## Commits ##
<details>
  <summary>Click to see details of commits</summary>
  <h3>Add web scraping functionality</h3>
  <ul>
    <li>Import lxml needs to be installed using <i>sudo apt-get install python3-lxml</i></li>
    <li>Inspect the elements of the webpage using right click -> inspect</li>
    <li>Using arrow in the top left hand corner of inspect</li>
    <li>Click element you need</li>
    <li>Right click the element and copy the full xpath</li>
    <li>Using <i>tree.xpath([path copied]/text())</i> and set equal to variable</li>
    <li>Variable will be a list</li>
    <li>Print first element of list</li>
  </ul>
  
  <h3>Add search functionality</h3>
  <ul>
    <li>Allow user to enter stock ticker</li>
    <li>Generate a URL by adding <i>/[stockTicker]-stock</i> to end of https://markets.businessinsider.com/stocks</li>
    <li>Use scraping methods from earlier to get stock prices</li>
  </ul>
  <h3>Add webscraping for tables</h3>
  <ul>
    <li>Allows user to enter name of company</li>
    <li>Shows in table form all stock tickers of companies that are returned</li>
    <li>Uses pandas to format data<i>sudo apt-get install python3-pandas</i></li>
    <li><i>displaySearch()</i> method found mostly from https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059</li>
  </ul>
  
  <h3>Add GUI</h3>
  <ul>
    <li>Add main.py file</li>
    <li>Going to be used for testing all the methods on the terminal</li>
    <li>Install tkinter <i>sudo apt-get install python3-tk</i></li>
    <li>Add GUI file</li>
    <li>Going to house all of the GUI that will call the methods</li>
    <li>Create basic GUI</li>
    <li>When a button is clicked makes call to <i>searchWebsite()</i></li>
    <li>Changes a label with the data received back from the method</li>
  </ul>
  
  <h3>Add Entry Box</h3>
  <ul>
    <li>When the button is clicked take data from the entry box</li>
    <li>Display the returned data in the label</li>
    <li>Add Listbox</li>
    <li>If a panadas dataframe is returned we display the data in a listbox rather than in text</li>
    <li><mark>Want to add the ability to select one item from the list box and click OK to submit</mark></li>
  </ul>
  <h3>Clear Listbox on Search</h3>
  <ul>
    <li>Simply clears the Listbox when a new stock is searched for</li>
  </ul>
  
  <h3>Allow selection from Listbox</h3>
  <ul>
    <li>When “ok” button is clicked we use a try-except statement</li>
    <li>If something in the Listbox is currently selected we do the search on that
      <ul>
        <li>Note: We do string manipulation to get the stock ticker from the end of the string selected</li>
      </ul>
    </li>
    <li>Otherwise we just search for what is currently in the textbox</li>
    <li>Also add code so that when a stock is searched from the Listbox selection, we replace the words in the entry box</li>
  </ul>
  
  <h3>Basic UI Changes</h3>
  <ul>
    <li>Change focus on the running of the application to the entry box</li>
    <li>Bind the enter key to the same function as clicking OK</li>
  </ul>
  
  <h3>Add Tests</h3>
  <ul>
    <li>Created file tests.py</li>
    <li>We run two tests on the search
       <ul>
         <li>First checks that when we type in APPL we get returned “The price of Apple (APPL) is”</li>
         <li>Second checks that if we type “apple” we got a pd dataframe </li>
      </ul>
    </li>
  </ul>
  
  <h3>Begin adding images</h3>
  <ul>
    <li>Adds some images so that an up or down arrow can be displayed</li>
  </ul>
  
  <h3>Add price increase or decrease </h3>
  <ul>
    <li>Add function <i>upOrDown()</i> in FinalProject.py which scrapes to see if there is an up or down arrow on the page        <ul>
      <li>Returns true if there is an up arrow or false if there is a down arrow</li>
      </ul>                                                                                                                 
    </li>
    <li>In GUI.py we add a new label called image</li>
    <li>We also add up and down arrow images as pgm 
      <ul>
        <li>Named <i>upArrow</i> and <i>downArrow</i></li>
      </ul>
    </li>
    <li>Call function <i>upOrDown()</i> and display the proper image using <i>image.config(image=[NameOfImage])</i></li>
  </ul>
  
  <h3>Add company class</h3>
  <ul>
  <li>On call to <i>searchWebsite()</i> an object of the company class is now returned
      <ul>
        <li>Returns true if there is an up arrow or false if there is a down arrow</li>
      </ul>                                                                                                                 
    </li>
    <li>In GUI.py we add a new label called image</li>
    <li>We also add up and down arrow images as pgm 
      <ul>
        <li>Company class contains the stock ticker, the company name and the price</li>
        <li>Soon to add whether the price of the stock is up or down </li>
      </ul>
    </li>
    <li>In the calls to searchWebsite() we now have to set it to an object
      <ul>
        <li>We then have to call the <i>getData()</i> on the class to print out the data like we did before</li>
      </ul>
    </li>
  </ul>
  
  <h3>Add check <i>upOrDown()</i> to <i>searchWebsite()</i></h3>
  <ul>
    <li>We are combining the <i>upOrDown()</i> method and the <i>searchWebsite()</i> 
        <ul>
          <li>This gets all the data at once so that multiple calls aren’t being done </li>
        </ul>                                                                                                               
    </li>
    <li>Had to add another attribute to the company class called <i>up</i> 
      <ul>
        <li>Had to account for this when creating a new class </li>
      </ul>
    </li>
    <li>When we want to use this data we just call <i>company.up</i> </li>
  </ul>
  
  <h3>Fix Layout and add price change</h3>
  <ul>
    <li>We now also grab the price change in both dollar amount and percentage  
        <ul>
          <li>These are added to the company class as a property call change</li>
        </ul>                                                                                                               
    </li>
    <li>Changed from using <i>pack()</i> to <i>grid()</i> 
      <ul>
        <li>Allows configuration of layout using <i>row=X</i> and <i>column =Y</i></li>
      </ul>
    </li>
    <li>Remove the pictures of the arrow
      <ul>
        <li>Instead we use text arrows</li>
        <li>Looks nicer and easier to deal with </li>
      </ul>
    </li>
    <li>Change the color of the text depending on if the price is up or down for the day
      <ul>
        <li>Use <i>fb=’[color]’</i></li>
      </ul>
    </li>
  </ul>
  
  <h3>Add news to Listbox on search of stock</h3>
  <ul>
    <li>When a stock is search displays news in the listbox  
        <ul>
          <li>Want to add that when you click on one you can somehow search?</li>
        </ul>                                                                                                               
    </li>
    <li>Need to fix when you enter a stock that searches website</li>
    <li>Need to fix some of the bad formatting </li>
  </ul>
  
  <h3>Split change to number and percent</h3>
  <ul>
    <li>We change the attribute <i>changeNumber</i> and <i>changePercent</i> 
        <ul>
          <li>Combine back together later</li>
        </ul>                                                                                                               
    </li>
    <li>When they were fetched together the program would fail when a search was done instead</li>
  </ul>
  
  <h3>Append url link to news</h3>
  <ul>
    <li>When we grab the news we now also want the link that it comes from</li>
    <li>In <i>displayNews()</i> method we grab all of the hrefs</li>
    <li> Then we create another column called <i>urls</i> for the dataframe
        <ul>
          <li>Just append the next href to this column every row of the table we loop through</li>
        </ul>                                                                                                               
    </li>
    <li>When iterating through the rows of the dataframe generate a dictionary
      <ul>
          <li>Contains both the title of the articles and the url</li>
      </ul> 
    </li>
    <li>Add a button called <i>search</i>
      <ul>
          <li>Set to disabled when there are search items in the listbox</li>
          <li>Set to enabled when there are news items in the listbox</li>
          <li>When click just prints the url in the terminal for now</li>
      </ul> 
    </li>
  </ul>
  
  <h3>Add Icon</h3>
  <ul>
    <li>Just adding an icon for the application</li>
  </ul>
  
  <h3>Small Changes</h3> 
  <ul>
    <li>Change the file path of icon</li>
    <li>Update loop for news from 1 to 0 to include all news articles</li>
  </ul>
  
  <h3>Launch browser on search click</h3> 
  <ul>
    <li>Uses <i>webbrowser.open(url,new=new)</i> to launch the browser with the URL of news article that is clicked</li>
    <li>Have to account for the edge case where the article is on their own website
      <ul>
        <li>They usually just point to the file</li>
        <li>We need to append https://markets.businessinsider.com to the beginning of the url and then it goes to the right place</li>
        <li>Just a simple if statement </li>
      </ul>
    </li>
  </ul>
  
  <h3>Fix button issues</h3> 
  <ul>
    <li>Add a global variable called <i>news</i>
      <ul>
        <li>Keeps track of if there is news in the listbox</li>
        <li>If there is news we make the enter button do a search</li>
      </ul>
    </li>
    <li>Also disable the “OK” button when the news is displayed</li>
    <li>Define a method called <i>callback</i> which is called every time something is changed in the textbox
      <ul>
        <li>We clear the listbox selection</li>
        <li>Re Enable the “OK” button</li>
        <li>Set news to false</li>
      </ul>
    </li>
    <li>Probably can eliminate the need for all of this we use just use two different listbox (for news and search).
      <ul>
        <li>Just hide them when they need to be</li>
      </ul>
    </li>
  </ul>
  
  <h3>Make multiple listbox</h3> 
  <ul>
    <li>Have news and searches in different listboxes
      <ul>
        <li>One is hidden and the other one is shown</li>
      </ul>
    </li>
    <li>Want to make it so the news are labels with buttons beneath </li>
  </ul>
  
  <h3>Start adding labels instead of listbox</h3> 
  <ul>
    <li>Instead of a listbox for news, we want labels 
      <ul>
        <li>Actually use messages</li>
        <li>Dynamically create labels (and buttons) for each of the news websites</li>
      </ul>
    </li>
    <li>Arranged in two columns </li>
    <li>As of right now buttons do nothing</li>
  </ul>
  
  <h3>Dynamically add buttons that go to websites</h3> 
  <ul>
    <li>Now add a command to each of the buttons
      <ul>
        <li>Calls <i>search()</i> method</li>
        <li>Uses lambda expression to assign the url needed</li>
      </ul>
    </li>
    <li>Fix url assignment
      <ul>
        <li>Was off by one</li>
      </ul>
    </li>
  </ul>
  
  <h3>Buttons display website name</h3> 
  <ul>
    <li>When we get title of news article and website, also grab the website name
      <ul>
        <li>Store as a separate column in pandas dataframe named “websites”</li>
      </ul>
    </li>
    <li>We assign this value to the title of the button</li>
  </ul>
  
  <h3>Fix parsing symbols</h3> 
  <ul>
    <li>Simply change <i>html.fromstring(page.content)</i> to <i>html.fromstring(page.text)</i></li>
  </ul>
  
  <h3>General UI Fixes and Part 2</h3> 
  <ul>
    <li>Add some padding to the news labels</li>
    <li>Change around stock, ticker, and prices</li>
  </ul>
  
  <h3>Fix File Structure</h3> 
  <ul>
    <li>Add folders to make application easier to understand
      <ul>
        <li>Had to change some of the imports in code</li>
      </ul>
    </li>
    <li>Add a few tests for <i>company</i> class</li>
    <li>Add comments for all methods</li>
  </ul>
  
  <h3>Small Fixes</h3>
  <ul>
    <li>Change the wrap size of the news articles</li>
    <li>Update file path in main.py</li>
  </ul>
  
  <h3>Add Screenshots</h3>
  <ul>
      <li>Add screenshots for the application for the GitHub page</li>
  </ul>
  
  <h3>Make Layouts Classes and Add Front Page</h3>
  <ul>
      <li><i>Example</i> class contains the main layout for the application</li>
      <li><i>CustomWidget</i> class contains the widget for displaying stock data
      <ul>
        <li>Label for stock name</li>
       <li>Label for stock price</li>
       <li>Label for stock price change</li>
      </ul>
      </li>
      <li>Front Page contatins data on DOW, S&P 500, and NASDAQ on page load</li>
  </ul>
  
  <h3>Fix Links</h3>
  <ul>
     <li>URLs off by one</li>
  </ul>
  
  <h3>Fix Testing</h3>
  <ul>
     <li>Had to fix import for WebScraping file</li>
  </ul>
  
  <h3>Fix edge case where stock does not have price data</h3>
  <ul>
     <li>Not all stocks have price data on this website</li>
     <li>Account for this by returning "No price data" if none is found in <i>WebScraping</i></li>
     <li>Have to account for this in the <i>GUI.py</i>
         <ul>
          <li>Just add an if statement to check if <i>company_data.price</i> is "No price data"</li>
          <li>Can then fix formatting accordingly</li>
         </ul>
     </li>
  </ul>
</details>
