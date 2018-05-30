#!/usr/bin/python
import sys
import subprocess
import os
import fileinput

def removeNewLine(s):
    if s.endswith('\n'):
        return s[:-1] 
    return s

while True:
    sys.stdout.write('\033[95m' + "level 1,\rHi game >" + '\033[94m')
    x = sys.stdin.readline()
    command = removeNewLine(x)
    try:
        y = subprocess.call(command, shell=True)
        n = subprocess.call("echo $PS1", shell=True)
        print os.getcwd()
        print n
        if command == 'cd ..':
            os.chdir('..')
        print y
    except Exception as e:
        print 'Exception: %s' % e
