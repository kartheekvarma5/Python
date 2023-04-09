from getpass import getpass

PassKey = getpass("Please Enter Your Password: ")

if PassKey == 'Hello':
    print("Key is Matching")
else:
    print("Key is not Matching")
