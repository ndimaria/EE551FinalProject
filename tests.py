import FinalProject as FP
import pandas as pd

def test_fetch():
    data = FP.searchWebsite("AAPL").split()
    data =  data[:-1]
    assert  data == ["The", "price", "of", "Apple", "(AAPL)", "is"]
def test_search():
    data = FP.searchWebsite("Apple")
    assert isinstance(data, pd.core.frame.DataFrame)
