try:
    Number = (int(input("Please input the no for which you want to see the tables: ")))
    StartRange = (int(input("Please input the Starting Range from which you want to start: ")))
    EndRange = (int(input("Please input the Ending Range from which you want to End: ")))

    print ("\n")
    for LoopValue in range( StartRange , (EndRange + 1 )):
        print (" {} X {} = {}".format(Number,LoopValue,( Number * LoopValue )))

except:
    Instructions = '''
    You have enter wrong value.. Possible Cases are as follows.. Please try again..
        1) You Might have entered a Alphabetical Character.
        2) You Might have entered a floating point no.
        3) You Might have entered a special/wild characters.
    '''
    print (Instructions)
