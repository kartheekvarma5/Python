import subprocess


def ECHO(message,file):

    CMD = 'echo'
    output = []
    
    WorkDone = subprocess.Popen([ CMD, message, file ], stdout = subprocess.PIPE)
    output = str(WorkDone.communicate())
    return output
    
#if __name__ == '__main__' :
    
#    file = testfile.txt
    
ECHO("HI","testfile.txt")
