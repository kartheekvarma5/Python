import os

for List in dir(os):
    if List.startswith("_") is False:
        print (List)