# EE551FinalProject #
This repository will contain code relevant to my EE551 Engineering Programming: Python class.

## Description ##
For this project I intend on creating a stock quote tracker. This application will allow a user to enter a symbol for a stock that they are curious about the price. The program will return the price possibly within a GUI that will have a green or red arrow depending on if the price is up or down for that day. In addtion, a user will be able to select how often they want to be notified about the stock price. The application will then emit a pop up or message with the stock price for every specified amount of time that the user wants.


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
</details>

