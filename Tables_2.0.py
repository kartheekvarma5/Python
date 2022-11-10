
def ForwardMultiply ( NumberValue , StartRangeValue, EndRangeValue ):
    for LoopValue in range( StartRangeValue , (EndRangeValue + 1 )):
        print ("\t\t{} X {} = {}".format(NumberValue , LoopValue, ( Number * LoopValue )))

def ReverseMultiply ( NumberValue , StartRangeValue, EndRangeValue ):
    while ( StartRangeValue >= EndRangeValue ):
        print ("\t\t{} X {} = {}".format(NumberValue , StartRangeValue, ( Number * StartRangeValue )))
        StartRangeValue = StartRangeValue - 1

try:
    Number = (int(input("\n Please input the No. for which you want to see the tables\t: ")))
    StartRange = (int(input(" Please input the Starting Range from which you want to start\t: ")))
    EndRange = (int(input(" Please input the Ending Range from which you want to End\t: ")))
    if ( StartRange <= EndRange ):
        ForwardMultiply( Number, StartRange, EndRange )
        print ("\n")
    elif ( StartRange > EndRange ):
        print ("\n\tPrinting the values in reverse Order\n")
        ReverseMultiply( Number, StartRange, EndRange )
        print ("\n")
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