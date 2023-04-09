import os 

if os.path.isdir('/root/test'):
    os.system('cp -rv /root/test /home/user/test')
else:
    print("File not exist")