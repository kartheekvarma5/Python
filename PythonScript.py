##========================= Python Scripting Tutorials Basics ==========================

a = 2
b = 3
c = 4

#Addition of a + b 
print (f"Addition of {a} + {b} is :", a + b )

#Substraction
print ("Substraction of", a, "-", b, "is :", a - b )

#Multiplication
print ("Multiplication of", a, "*", b, "is :", a * b )

#Division
print (f"Division of {a} / {b} is :", a / b )

#Square
print ("Square of", a, "**", b, "is :", a ** b )

#Modulus
print ("Modulus of", c, "//", a, "is :", c // a )

#Absolute Value of (-3) is
#Example
#births = 4
#print("No. of Births Today is(are): {} births".format(births))
print ("Absolute value of (-3) is: {} ".format(abs(-3)))
#Above can be written as below (it is simple way as we learnt it long back. Above is another way with formatting
print ("Absolute value if (-3) is:", abs(-3))

var1,var2,var3 = 10,20,30   #Python supports multiple variable loading in a single line and is acceptable in python.

SUM=var1+var2           #We can do Addition of Two variables while loading into another variable in python (mostly same as bash scripting)
MUL=var1*var3
DIV=var3/var2
print (var1,var2,var3)  

print (SUM,MUL,DIV)     #To display multiple variables at a time same as how we displayed message and Variable
print (10*20+30)        #Writing this way sometimes gives wrong output so make sure you use below paranthesis for proper output
print ((10*20)+30)

#Strings
X = "Hai"               #You Should Always use Double/single Quotation if any Variable data is a string even it is caps or small else it work load and you will get errors
Y1 = "How"
Z = "Are You"

print (X,Y1,Z)

Data = '''
In Python if any Variable is Started and Ended with three Single Quotes and contains Some data in between it will be added in to that variable.
To display Content we need to use print (variable) to display the content of it it is useful to save any data or something.
This is same like how we write <<<MESSAGE and end with MESSAGE in Bash
'''
print (Data)

temp="temporary"
#Check Type of any variable or Output
print (type(123))
print (type(1.0980803))
print (type("Kartheek1"))
print (type(temp))

Name1 = "Kartheek "
Name2 = "Varma"
print (Name1+Name2)     #In Python we can do contatenation of two or more strings by simply adding +
#print (Name1+100)       #This Gives Error Because Here the Name1 Variable is string and 100 is int so this will not work in python so you need to make 100 value in to strings to display it
#How can you make an int value to string (Ans: Just Add Single/Double Quotes while loading into a variable/ while printing)
Value='100'
Val=100
print (Name1+Value)
print (Name1+'200')
#print (Name1+Val)          #This is wrong and gives error as cannot concatenate String and Integer
#There are some other ways we can convert int value to String and Vice versa. We can see it in later section. For Temporarily Just Stick for sometime.

#Now What is the recommended way how can you convert it.
#We need to use str(int_value) to convert int value to string

#str(100)       #Now 100 is String, How to know it is converted or not use print (type(str(100)) to check it
print (str(Value))
print (type(str(Value)))

Value1=str(Value)
print (Value1)
print (Name1+Value1)
#We can convert Few strings to int values using int(str_value). But not sure on which string values it works check once in internet or python docs once.

#Escape Sequences (If we use single or Double Quote in Words we may sometimes get error how to avoid those in python

#tmp1='I'm Engineer'     //This Gives Error Where the ' is getting ended and started to avoid this problem we need to use back slash
tmp1='I\'m Engineer'
print (tmp1)

#How to display a backSlash in print Statement since it is used as a escape sequence character. You need to put one more back Slash before a back slash to make it appear
#tmp2='BackSlash Symbol is \'     #This Gives Error
tmp3='BackSlash Symbol is \\'     #This Works
print (tmp3)

name = "Babu"
age = "30"

print ("Hi", name, "Your age is :", age )       #This we have seen earlier but it is difficult to write and maintain the commas so we use formatting as follows
#Formatting
print ("Hi {} Your Age is : {}".format(name,age))
print ("Hi {} Your Age is : {}".format("bambu",age))
print ("Hi {} Your Age is : {}".format(name,100))
print ("Hi {name_val} Your Age is : {ageval}".format(name_val="Bro",ageval=20))
print ("Hi {0} Your Age is : {1}".format(name,age))
print ("Hi {1} Your Age is : {0}".format(name,age))

var="abcdefg"
print (var[0])      #TO Print only the first letter in that variable Ans : a
print (var[0:3])    #Here we are using a range to print the letters. Here Zero Means Start from ) field that is a and print 3 letters from that that is 1(that is starting of this variable)  Ans: abc
print (var[1:3])    #Here we are using a range to print the letters. Here One Means Start from 1st Letter and print 3 letters from a(Starting of variable) Ans: bc
print (var[0:])     #Here we are using a range to print the letters. Here Zero Means Start from a and print NULL (denotes till end) Ans: abcdefg
print (var[4:])     #Here we are using a range to print the letters. Here Four Means Start from d and print NULL (denotes till end) Ans: efg
print (var[:5])    #This print Starting to 10 letters in that variable.

#Boolean
var1 = True
var2 = False        #Boolean Values cannnot be enclosed in quotation, if done so it is not a bool data type and is considered as String data type.
var3 = "True"

print (type(var1))
print (type(var3))

#How to make 1 and 0 as True and False in boolean. Since 1 and 0 are int data type

Bool1 = bool(0)
Bool2 = bool(1)
print (type(Bool1), Bool1)
print (type(Bool2), Bool2)

#can we load int, bool, float, string in alist to single variable ? Yes

List = [ "hi" , True , 1.34 , 12 ]

print (List)
print (type(List))
#You can filter with field how we extracted using 0,1,2 like that. To Read the values.
print (List[0])
print (type(List[0]))
print (List[1])
print (type(List[1]))
print (List[1:3])
print (type(List[1:3]))

#List Methods// Comment using three single quotes
'''
https://www.w3schools.com/python/python_lists_methods.asp
---------------------------------------------------------------
Method		Description
---------------------------------------------------------------
append()	Adds an element at the end of the list
clear()		Removes all the elements from the list
copy()		Returns a copy of the list
count()		Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()		Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()		Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()		Sorts the list
---------------------------------------------------------------
Refer Above Link
'''
matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
print (matrix)
print (matrix[0][1:3])

#NoneType
nonetype = None
print (None)
print (type(None))
print (type(nonetype))

#Above None Type is having no value. That means the value is not set
#Dictionary // Dictionary starts with flower braces and also consists in Array. Where array/list starts with Square braces.

Dict1 = {
        "Name":"Kartheek",
        "Age":10
        }

print (Dict1)
print (Dict1["Name"])

Dict2 = [
        1,2,{
            "Name":"Varma",
            "PIN":516100
            }
        ]

print (Dict2)
print (Dict2[2]["PIN"])

#Python Dictionary Methods
#For more knowledge (https://www.w3schools.com/python/python_ref_dictionary.asp)
'''
---------------------------------------------------------------
Method			Description
---------------------------------------------------------------
clear()			Removes all the elements from the dictionary
copy()			Returns a copy of the dictionary
fromkeys()		Returns a dictionary with the specified keys and value
get()			Returns the value of the specified key
items()			Returns a list containing a tuple for each key value pair
keys()			Returns a list containing the dictionary's keys
pop()			Removes the element with the specified key
popitem()		Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()		Updates the dictionary with the specified key-value pairs
values()		Returns a list of all the values in the dictionary
---------------------------------------------------------------
Refer Above Link
'''
#IF Condition
val1 = 10
val2 = 3
val3 = 100

if ( val1 > val2 ):
    print ("{} is Larger than {}".format(val1,val2))
else:
    print ("{} is Smaller than {}".format(val1,val2))

if ( val1 == val3 ):
    print ("{} is Equals to {}".format(val1,val3))
elif ( val1 < val3 ):
    print ("{} is Smaller than {}".format(val1,val3))
else:
    print ("{} is Something else".format(val1))

#For Loop
for i in (1,2,3,4,"Hello",True):
    print (i)

#For Loop with Range
for i in range(0,10):       #Output will be 1-9 
    print (i)

for k in range(1,11):       #Output will be 0-10 (Python COnsider Last Range as (n-1) Same how we seen in earlier section
    print (k)

#While Loop
i = 1
while (i < 5 ):
    print (i)
    i = i + 1

#While with Break
i = 1
while (i < 10 ):
    print (i)
    i = i + 1
    if ( i == 5 ):
        print (i)       #Here print statement is required Just to print the value 5 , Else it will skip
        break

#While with Continue
i = 0
while (i < 10 ):
    i = i + 1
    if ( i == 5 ):
        print (i)       #Here print statement is required Just to print the value 5 , Else it will skip
        continue
    print (i)

#How to print 5 Value also and moreover if you have any dummy if condition and you just need your while or if condition to pass instead taking any action you can add pass after if condition as below
#While with Pass
i = 0
while (i < 10 ):
    i = i + 1
    if ( i == 5 ):
        pass
    print (i)

#functions
def function1():
    A = 0
    print ("I am in function1")
    return A

#print (A)       #This will not get the value from function1
function1()     #This will just get print statement from function1
print (function1())     #This will print statement from function1 along with A value

def function2(var1,var2):
    B = 0
    print ("I am in function2")
    return B+var1+var2

print (function2(10,20))

#xargs in functions (Used to show multiple parameters/variables to pass and display)
value3=30
def function3(*xargs):
    print ("I am in function3")
    print (xargs)
    #print (xargs[2])           #You can filter the required value also by using square braces

function3(10,20,value3,"Hello")

#By Using xargs you can pass variables and values but if you want to pass some/define variables while passing it wont work.
#To overcome we need to use "kwargs"

value3=30
def function4(**kwargs):
    print ("I am in function4")
    print (kwargs)
    #print (kwargs[value1])                 #You can just extract the required key and its value. Same how we did for a dictionary/array.

function4(value1="Hai",value2="Hello")      #You need to use double stars(**) for kwargs

value3=30
def function5(*args,**kwargs):              #You need to use double stars(**) for kwargs
    print ("I am in function5")
    print (args)                            #if you just use this you can see values instead keyvalue pairs
    print (kwargs)                          #if you just use this you can see keyvalue pairs
                                            #if you enable both you will get both outputs
function5(10,20,30,value1="Hai",value2="Hello")      

#Passing Values from Outside to Python Script
#input("Please Enter your Name: ")

#To Load to variables and make use in script use as below
Name = input("Please Enter your Name: ")
print (Name)

#To load int value instead others
Age = int(input("What is your age?: "))
print (Age)                                 #Here if you give age properly in int data type it prints, But if you give string data type or string it gives error so we need to do error handling now.

#Error Handling
try:
    Age = int(input("What is your age?: "))
    print (Age)
except:
    print ("You Entered a Wrong Value or You entered in different Format!!")

#More Reading from "https://www.w3schools.com/python/python_try_except.asp"

#Packages in Python
#We can use "import <file.file1>" and from "<file> import * " to load data from another files.

#Sample files with dir structure (main.py || first.py || functions/{function1.py,function2.py})
#file1
value1 = 10

#function/function1
def fun1():
    print ("This is function1")

#main.py
from asyncore import write
from doctest import testfile
import file1
import functions.function1
#from file1 import *        #Use it when you dont want to mention first.value1 every time you can just mention value1 in main.py
#import functions           #This is wrong you cannoy load multiple files in a directory with just sepcifying the folder name. You must specify the name everytime.

print ("I am in Main.py")
print ("I am in first.py: ", first.value1)
#print ("I am in first.py:, value1")     #When we use "from file1 import * " in main.py
functions.function1.fun1()              #To call a function

#Python Tutorial Examples https://www.w3schools.com/python/default.asp

#Reading the Files using Python
cat testfile.txt
Hi Hello
Last Line

R = open("testfile.txt","r")
R(read(testfile.txt))
print (R(read(testfile.txt)))

#Writing the content to file using python
W = open("testfile.txt","w")
W(write(testfile.txt))
print (W(read(testfile.txt)))
#Here once you use write function it is still open you need to close the file once data is written so use close function for it
W.close()

#Write and Read
W = open("testfile.txt","w")
W(write(testfile.txt))
content = "some content"
print (W(read(testfile.txt)))
W.close()
print(R.read())

#================ END OF BASIC PYTHON SCRIPTING ========================