#!/usr/bin/python
import sys
import subprocess
import os
import fileinput
import time
from consts import IN_WIDTH
from utils import removeNewLine
class InvalidArgument(Exception):
    pass
    
prompt = '\033[95m' + "level 1 Hi game >" + '\033[94m'

def addPrompt(totalout_lines, prompt): 
    totalout_lines.append('\033[95m' + "level 1 Hi game >" + '\033[94m')

def addUserInput(cmd, totalout_lines):
    totalout_lines[-1] = fill_line(totalout_lines[-1] + cmd , c=".", compensation = 10)

def fill_line(l, c=' ', in_width=IN_WIDTH, compensation = 0):
    if len(c) != 1:
        raise InvalidArgument
    return l + c * ((in_width-len(l)) + compensation)

def addOutput(output, totalout_lines, in_width=IN_WIDTH):
    lines = output.split("\n")
    filled_lines = []
    for l in lines:
        if len(l) < in_width and l != '':
            filled_lines.append(fill_line(l, c = "."))
    totalout_lines += filled_lines

def render_totalout(totalout_lines, prompt=True):
    final_screen_lines = totalout_lines
    final_screen = "\n".join(final_screen_lines) + ("\n" if not prompt else "")
    return final_screen
    
def cleanScreen():
    subprocess.call("clear", shell=True)
    subprocess.call("printf '\e[3J'", shell=True)

def turn(totalout_lines):
    addPrompt(totalout_lines, prompt)
    cleanScreen()
    sys.stdout.write(render_totalout(totalout_lines, True))
    userInput = sys.stdin.readline()
    addUserInput(removeNewLine(userInput), totalout_lines)
    command = removeNewLine(userInput)
    try:
        process = subprocess.Popen(command, shell=True,
                                            stdout=subprocess.PIPE, 
                                            stderr=subprocess.PIPE)
        out, err = process.communicate()
        if out:
            addOutput(out, totalout_lines)
        elif err:
            addOutput(err, totalout_lines)
        sys.stdout.write(render_totalout(totalout_lines, False))
        # errcode = process.returncode
        if command == 'cd ..':
            os.chdir('..')
        turn(totalout_lines)
    except Exception as e:
        print 'Exception: %s' % e        

if __name__ == '__main__':
    turn([])