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