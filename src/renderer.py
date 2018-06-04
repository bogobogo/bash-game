import sys
import subprocess

messages = {"progress_bar": {"message": '', 
                             "startPosition": (0,0),
                             }}
                             
def setTerminalSize(x, y):
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=y, cols=x))
def cleanScreen():
    subprocess.call("clear", shell=True)
    subprocess.call("printf '\e[3J'", shell=True)
def goto(x, y):
    """ Moves curser to a position relative to current top of screen """
    subprocess.call("tput cup %d %d" % (y, x), shell=True)
def saveCursorPosition():
    subprocess.call("tput sc", shell=True)
def restoreCursorPosition():
    subprocess.call("tput rc", shell=True)
def echoMessage(message):
    """ Used for message writing after moving the cursor """
    subprocess.call("echo '" + message + "'", shell=True)
def write(message):
    """ default stdout message """    
    sys.stdout.write(message)
def printMessage(message):
    """ Used for elaborate ASCII messages """
    subprocess.call(["printf $'" + message + "'", "-n"] , shell=True)
def printMessageAt(message, location):
    saveCursorPosition()
    goto(location[0],location[1])
    printMessage(message)       
    restoreCursorPosition()




