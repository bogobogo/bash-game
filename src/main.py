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

# def render_totalout(totalout_lines, prompt=True):
#     final_screen_lines = addGameMessage(totalout_lines, "hello")
#     final_screen = "\n".join(final_screen_lines) + ("\n" if not prompt else "")
#     return final_screen

def turn(totalout_lines):
    totalout_lines = []
    addPrompt(totalout_lines, prompt)
    renderer.write(prompt)
    progressBar.write()
    level1_firstMessage.write()
    # renderer.printMessageAt(first_message, (50, 50))       
    # renderer.printMessageAt(first_message, (50, 50))       
    userInput = sys.stdin.readline()
    addUserInput(removeNewLine(userInput), totalout_lines)
    level1_firstMessage.erase()
    userInput = sys.stdin.readline()
    # command = removeNewLine(userInput)
    # try:
    #     process = subprocess.Popen(command, shell=True,
    #                                         stdout=subprocess.PIPE, 
    #                                         stderr=subprocess.PIPE)
    #     out, err = process.communicate()
    #     if out:
    #         addOutput(out, totalout_lines)
    #     elif err:
    #         addOutput(err, totalout_lines)
    #     sys.stdout.write(render_totalout(totalout_lines, False))
    #     # errcode = process.returncode
    #     turn(totalout_lines)
    # except Exception as e:
    #     print 'Exception: %s' % e        

if __name__ == '__main__':
    renderer.cleanScreen()
    subprocess.call("tput cup 0 1", shell=True)
    turn([])

## if command == 'cd ..':
            # os.chdir('..')