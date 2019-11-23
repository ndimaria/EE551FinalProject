import FinalProject as FP

"""
We want to run this loop until they type 'exit'
"""
while(1):
    searchTerm = input("What stock are you looking for: ")
    if (searchTerm ==  "exit"):
        break
    company = FP.searchWebsite(searchTerm)
    print(company, end = '\n')
    print(company.change)
    #print(FP.searchWebsite(searchTerm) ,end = '\n\n')
    #print(FP.upOrDown(searchTerm), end = '\n')
