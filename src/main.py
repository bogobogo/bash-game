#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sys
import subprocess
import os
import fileinput
import time
import renderer
from consts import IN_WIDTH, TESTING
from utils import removeNewLine
from messages import level1_firstMessage, progressBar, totalxp
from strings import first_message

getUserInput = lambda: sys.stdin.readline()
class InvalidArgument(Exception):
    pass
    
prompt = '\033[95m' + "level 1 Hi game >" + '\033[94m'

def addPrompt(totalout_lines, prompt): 
    totalout_lines.append('\033[95m' + "level 1 Hi game >" + '\033[94m')

def addUserInput(cmd, totalout_lines):
    totalout_lines[-1] = fill_line(totalout_lines[-1] + cmd , c=" ", compensation = 10)

def fill_line(l, c=' ', in_width=IN_WIDTH, compensation = 0):
    if len(c) != 1:
        raise InvalidArgument
    return l + c * ((in_width-len(l)) + compensation)

def addOutput(output, totalout_lines, in_width=IN_WIDTH):
    lines = output.split("\n")
    filled_lines = []
    for l in lines:
        if len(l) < in_width and l != '':
            filled_lines.append(fill_line(l, c = " "))
    totalout_lines += filled_lines


def turn(totalout_lines, n=0):
    addPrompt(totalout_lines, prompt)
    renderer.write(prompt)
    userInput = getUserInput()
    command = removeNewLine(userInput)
    addUserInput(command, totalout_lines)
    try:
        process = subprocess.Popen(command, shell=True,
                                            stdout=subprocess.PIPE, 
                                            stderr=subprocess.PIPE)
        out, err = process.communicate()
        subprocess.call("tput civis", shell=True)
        totalxp.clean(totalout_lines)    
        progressBar.clean(totalout_lines)
        level1_firstMessage.clean(totalout_lines)
        if out:
            addOutput(out, totalout_lines)
            renderer.write(out)
        elif err:
            addOutput(err, totalout_lines)
            renderer.write(err)
        totalxp.overlay(totalout_lines)    
        progressBar.overlay(totalout_lines)
        level1_firstMessage.overlay(totalout_lines) 
        subprocess.call("tput cnorm", shell=True)   
        turn(totalout_lines, n=n+1)
    except Exception as e:
        print 'Exception: %s' % e        

if __name__ == '__main__':
    renderer.cleanScreen()
    # subprocess.call("tput cup 0 1", shell=True)
    renderer.setTerminalSize(150, 150)
    totalxp.overlay([])    
    progressBar.overlay([])
    level1_firstMessage.overlay([])
    turn([])

## if command == 'cd ..':
            # os.chdir('..')