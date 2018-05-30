import sys
import subprocess
import os
import fileinput
def removeNewLine(s):
    if repr(s)[-3:-1] == '\\n':
        return repr(s)[1:-3]
    return str(s)

sys.stdout.write('\033[95m' + "level 1, game >" + '\033[94m')
x = sys.stdin.readline()
print len(x)
print repr(x)[1:-3]
print repr(x)[-3:-1] == "\\n"
sys.stdout.write(removeNewLine(x))
#print x[0:-3]
y = subprocess.check_output([removeNewLine(x)])
print y
#print os.environ['HOME']
#print subprocess

