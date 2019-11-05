import FinalProject as FP

"""
We want to run this loop until they type 'exit'
"""
while(1):
    searchTerm = input("What stock are you looking for: ")
    if (searchTerm ==  "exit"):
        break
    print(FP.searchWebsite(searchTerm) ,end = '\n\n')
