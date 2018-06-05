#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sys
import subprocess
import os
import fileinput
import time
import renderer
from consts import IN_WIDTH
from utils import removeNewLine
from messages import level1_firstMessage, progressBar
from strings import first_message
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

def turn():
    renderer.write(prompt)
    userInput = sys.stdin.readline()
    command = removeNewLine(userInput)
    try:
        process = subprocess.Popen(command, shell=True,
                                            stdout=subprocess.PIPE, 
                                            stderr=subprocess.PIPE)
        out, err = process.communicate()
        subprocess.call("tput civis", shell=True)
        progressBar.erase()
        level1_firstMessage.erase()
        if out:
            renderer.write(out)
        elif err:
            renderer.write(err)
        # errcode = process.returncode
           
        progressBar.write()
        level1_firstMessage.write() 
        subprocess.call("tput cnorm", shell=True)   
        turn()
    except Exception as e:
        print 'Exception: %s' % e        

if __name__ == '__main__':
    renderer.cleanScreen()
    # subprocess.call("tput cup 0 1", shell=True)
    progressBar.write()
    level1_firstMessage.write()
    turn()

## if command == 'cd ..':
            # os.chdir('..')