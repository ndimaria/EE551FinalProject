import FinalProject as FP
import pandas as pd
from difflib import SequenceMatcher

"""
We want to check that all of the data is returned from the website
This is for when there is actually stock_data
"""
def test_fetch():
    company_data = FP.searchWebsite("AAPL")
    assert company_data.stock_ticker == "AAPL" 
    assert company_data.name == "Apple"
    assert float(company_data.price) >= 0
    assert isinstance(company_data.news, pd.core.frame.DataFrame)
    assert company_data.up == False or company_data.up == True
    s_1 = company_data.change
    s_2 = "200.00 (1.10%)"
    assert SequenceMatcher(a=s_1,b=s_2).ratio()>.40

"""
This will check if we do a search instead that a DataFrame is returned
"""
def test_search():
    data = FP.searchWebsite("Apple")
    assert isinstance(data, pd.core.frame.DataFrame)
    
    

