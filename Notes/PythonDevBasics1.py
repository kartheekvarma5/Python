print ("Hello World")
a,b,c=10,20,30
print (a)
print (b)
print (c)
print (a+b+c)

#C/Java Declaration (Static Typed Programming Language)
#int a=10;
#bool b=true;

#Python (Dynamic Typed Programming Language)
#a=10
#b=True

a=10
b=True
type (a)//type(a)
type (b)

a=10
b=20
print (a+b)
print (a-b)
print (a*b)
print (a/b)

print ("Addition of",a,"and",b,"is:",a+b)

Generate Single Random OTP
from operator import truediv
from random import *
print (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

Generate 10 Random OTP's
from random import *
for i in range(10):
	print (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

#Python 2.0 Code Syntax
#print "Hello"

#Python 3.0 Code Syntax
print("Hello")

#  File "<stdin>", line 1
#    print "Hello"
#    ^^^^^^^^^^^^^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

X=10					// Here X is a Variable name which is an identifier
def f1():				// Here f1 is a function name which is an identifier
pass
class Test1(Exception):	// Here Test1 is a Class name which is an identfier 

cash=10
print (cash)
10
cash
10
ca$h=10
  File "<stdin>", line 1
    ca$h=10
      ^
SyntaxError: invalid syntax

total123=10
123total=100
  File "<stdin>", line 1
    123total=100
      ^
SyntaxError: invalid decimal literal

hello=20
HELLO=30
print (hello)
20
print (HELLO)
30

x=20
print (x)
if=30
  File "<stdin>", line 1
    if=30
      ^
SyntaxError: invalid syntax
def=40
  File "<stdin>", line 1
    def=40
       ^
SyntaxError: invalid syntax


xyz=900
print (xyz)
900
kartheekvarma=123
print (kartheekvarma)
123
_abc_abc=23
print (_abc_abc)
23
Hello2Hai=45
print (Hello2Hai)
45


a=True
a
True
a=true
a
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
b=None
b
b=none
b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'none' is not defined. Did you mean: 'None'?

import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

a=10
print(a)
10
type(a)
<class 'int'>
id(a)
2190496498192
=====================
#Count 1-20 in same position
import time
for i in range(1,21):
    time.sleep(0.5)
    print(i, end='\r')  #Return carriage at same line.

#Linux Commands
import os
os.system('dir H:\Kartheek\DevOps\Python')

#mailing
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('fromemailid@gmail.com', 'password')
server.sendmail('fromemailid@gmail.com', 'toemailid@gmail.com', 'Message Body')

for i in range(4):
    for j in range(4):
        print('*', end=" ")
    print()

* * * * *
* * * * *
* * * * *
* * * * *


for i in range(1,11,2):
    print(i)

    Print 1 to 10 but skip 2 numberss before printinf.. Also you can say print odd numbers

for i in range(11,1,-1):
    print(i)

print in reverse order

i=1
while i<=5:
    print ('Kartheek ',end="")
    j=1
    while j<=4:
        print ('varma ', end="")
        j = j + 1
    i = i + 1
    print()
	
Kartheek varma varma varma varma 
Kartheek varma varma varma varma 
Kartheek varma varma varma varma 
Kartheek varma varma varma varma 
Kartheek varma varma varma varma 

for i in range(4):
    print('*', end=" ")
    for j in range(4):
        print('*', end=" ")
    print()

* * * * *
* * * * *
* * * * *
* * * * *

==========================