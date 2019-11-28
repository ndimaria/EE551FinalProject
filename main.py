import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'CodeFiles')

import WebScraping as FP
import pandas as pd

"""
We want to run this loop until they type 'exit'
This is non the GUI version of the application
"""
while(1):
    searchTerm = input("What stock are you looking for: ")
    if (searchTerm ==  "exit"):
        break
    company = FP.searchWebsite(searchTerm)
    print(company, end = '\n')
    if (isinstance(company, pd.core.frame.DataFrame)):
    	print("Which company would you like:")
    else:
    	with pd.option_context('display.max_rows',None, 'display.max_columns',None,'display.max_colwidth', -1):
    		print(company.news)

