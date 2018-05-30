import sys
import subprocess
import os
import fileinput
sys.stdout.write('\033[95m' + "level 1, game >" + '\033[94m')
x = sys.stdin.readline()
y = subprocess.check_output(["ls"])
print y
print os.environ['HOME']
print subprocess
sys.stdout.write("${ret_status} %{$fg[cyan]%}%c%{$reset_color%} $(git_prompt_info)")

print sys.argv[1]
