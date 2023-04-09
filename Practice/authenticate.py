from getpass import getpass
from colorama import Fore, Back, Style

UserName = str(input(Fore.MAGENTA + "Please enter Username : " + Style.RESET_ALL))
Password = getpass(prompt=Fore.MAGENTA + "Please enter your password: " + Style.RESET_ALL)
# Password = getpass.getpass(prompt=Fore.YELLOW + "Please enter your password: " + Style.RESET_ALL)
# If you directly use "import getpass"
if UserName == 'kartheek' and Password == 'Test@123':
    print(Fore.GREEN + Back.CYAN + "\n\tPassword is matching..Welcome to Python World" + Style.RESET_ALL)
else:
    print(Fore.RED + Back.CYAN + "\n\tAuthentication Failure..Please try again..Bye" + Style.RESET_ALL)

'''
With Function
from getpass import getpass
from colorama import Fore, Back, Style

def Authenticate(UserName,Password):
    if UserName == 'kartheek' and Password == 'Test@123':
        print(Fore.GREEN + "\n\tPassword is matching..Welcome to Python World" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n\tAuthentication Failure..Please try again..Bye" + Style.RESET_ALL)

UserName = (str(input(Fore.YELLOW + "Please enter Username : " + Style.RESET_ALL )))
Password = getpass(prompt=Fore.YELLOW + "Please enter your password: " + Style.RESET_ALL)
# Password = getpass.getpass(prompt=Fore.YELLOW + "Please enter your password: " + Style.RESET_ALL)
# If you directly use "import getpass"

Authenticate(UserName,Password)
'''
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

