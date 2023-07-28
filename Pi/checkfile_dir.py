import os

InputFileDir = input("Please Enter File/Directory Name to check its availability : ")
FileDir = InputFileDir.removeprefix('"').removesuffix('"')

if os.path.exists(FileDir):
    if os.path.isdir(FileDir):
        print ("Found [ {} ] and it is a Directory".format(FileDir))
    elif os.path.isfile(FileDir):
        if os.path.getsize(FileDir) <= 0 :
            print ("Found [ {} ] and it is an Empty File..Size is [{}]".format(FileDir,os.path.getsize(FileDir)))
        elif os.path.getsize(FileDir) > 0 :
            print ("Found [ {} ] and it is a non-Empty File..Size is [{}]".format(FileDir,os.path.getsize(FileDir)))
    else:
        print ("Something went wrong while checking File/Folder..", [FileDir])
else:
    print ("Not Able to Found File/Directory", [FileDir])
