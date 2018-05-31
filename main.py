#!/usr/bin/python
import sys
import subprocess
import os
import fileinput
import time

#for i in range(10):
#        sys.stdout.write("\r{0}>".format("="*i))
#        sys.stdout.flush()
#        time.sleep(0.5)

def removeNewLine(s):
    if s.endswith('\n'):
        return s[:-1] 
    return s
totalout = ""
prompt = '\033[95m' + "level 1 Hi game >" + '\033[94m'
while True:
    # sys.stdout.write("clear && printf '\e[3J')
    subprocess.call("clear", shell=True)
    subprocess.call("printf '\e[3J'", shell=True)
    totalout = totalout + prompt
    # sys.stdout.flush()
    sys.stdout.write(totalout)
     
    x = sys.stdin.readline()
    totalout = totalout + x  
    command = removeNewLine(x)
    try:
        process = subprocess.Popen(command, shell=True,
                                        stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE)
        out, err = process.communicate()
        totalout = totalout + out
        # sys.stdout.flush()
        sys.stdout.write(totalout) 
        # print out
        sys.stdout.write(err) 
        errcode = process.returncode
        if command == 'cd ..':
            os.chdir('..')
    except Exception as e:
        print 'Exception: %s' % e
