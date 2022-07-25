def ForwardMultiply ( NumberValue , StartRangeValue, EndRangeValue ):
    for LoopValue in range( StartRangeValue , (EndRangeValue + 1 )):
        print (" {} X {} = {}".format(NumberValue , LoopValue, ( Number * LoopValue )))

def ReverseMultiply ( NumberValue , StartRangeValue, EndRangeValue ):
    while ( StartRangeValue >= EndRangeValue ):
        print (" {} X {} = {}".format(NumberValue , StartRangeValue, ( Number * StartRangeValue )))
        StartRangeValue = StartRangeValue - 1

try:
    Number = (int(input("\n Please input the no for which you want to see the tables: ")))
    StartRange = (int(input(" Please input the Starting Range from which you want to start: ")))
    EndRange = (int(input(" Please input the Ending Range from which you want to End: ")))
    
    print ("\n")
    if ( StartRange <= EndRange ):
        ForwardMultiply( Number, StartRange, EndRange )
    elif ( StartRange > EndRange ):
        print ("\tPrinting the values in reverse fashion\n")
        ReverseMultiply( Number, StartRange, EndRange )

        # RevInput = str(input("\tYou have given start range lesser than end range, Please make sure you give StartRange as Lower than EndRange..\n\tDo you want to continue and show the tables in reverse order?[Yes/No]: "))    
        # if (( RevInput.casefold() == "Yes" or RevInput.casefold() == "Y" )):
        #     RevInput = "yes"
        #     print (RevInput)
        #     ForwardMultiply( Number, StartRange, EndRange )
        # else:
        #     print ("Hello")

    else:
        print ("\tSomething went wrong. Please check the same..")

except RevInput as str:
    Instructions = '''
    You have enter wrong value.. Possible Cases are as follows.. Please try again..
        1) You Might have entered a Alphabetical Character.
        2) You Might have entered a floating point no.
        3) You Might have entered a special/wild characters.
    '''
    print (Instructions)
