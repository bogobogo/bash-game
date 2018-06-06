import sys
import subprocess
import itertools
from consts import IN_WIDTH

fillIn = " " * IN_WIDTH

def setTerminalSize(x, y):
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=y, cols=x))

def getTerminalSize():
    x = subprocess.check_output("tput cols", shell=True)
    y = subprocess.check_output("tput lines", shell=True)
    return (int(x), int(y))

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

def getRelevantHistoryLines(line_history, scrn_height, msg_len, startY):
    line_history_first_line_pos = len(line_history) - (scrn_height - startY) + 2
    line_history_last_line_pos = line_history_first_line_pos + msg_len - 1
    history_lines_to_add = line_history[line_history_first_line_pos: line_history_last_line_pos]
    return history_lines_to_add

def historyCoversScreen(line_history, scrn_height):
    return len(line_history) >= scrn_height

def historyAndMsgIntersect(line_history, startY):
    return len(line_history) > startY

def combinedMessages(msg_lines, history_lines):
    if len(msg_lines) > len(history_lines):
        return msg_lines[0] + '\n' + '\n'.join([line + msg_line for line, msg_line in list(itertools.izip_longest(history_lines, msg_lines[1:], fillvalue=fillIn))])
    else:
        raise ValueError('message length should always be longer than the history lines to combine')
def combineHistoryAndMessage(message, starting_line, line_history, scrn_height):
    if historyCoversScreen(line_history, scrn_height):
        msg_len = len(message)
        # Since pressing enter pushes everything a line up in a full screen we deduce it by 1
        starting_line = starting_line - 1
        history_lines_to_add = getRelevantHistoryLines(line_history, scrn_height, msg_len, starting_line)
        if len(history_lines_to_add) != msg_len - 1:
            raise ValueError('message length be 1 less when historyCoversScreen')
        return combinedMessages(message, history_lines_to_add)
    elif historyAndMsgIntersect(line_history, starting_line):
        msg_len = len(message)
        history_lines_to_add = line_history[starting_line + 1: starting_line + msg_len]
        return combinedMessages(message, history_lines_to_add)
    else: 
        return combinedMessages(message, [])




