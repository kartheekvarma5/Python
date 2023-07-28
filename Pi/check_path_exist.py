import os
#Read User Input
UserInput= input("Please enter the path to check: ")
if os.path.exists(UserInput):
    print ("Path (",UserInput,") Exists")
else:
    print ("Path (",UserInput,") NotExists")