# -*- coding: utf-8 -*-
import subprocess
import os

#### welcome to syshero - a multiplayer game world where you cooperate and compete with others to gain reputation and resources,
#  using unix knowledge. no prior knowledge is required. you will enter the multiplayer world when you reach level 10.
#  to get Started create your character
# Name:
#
# 
#to enter the world press y 
#### use 
#


progressBar = "██████████████████████████████████████████████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"

first_message_content = """ 
Hey Dan. You don\\'t know me, but I need your   
help.                                           
I wish I could tell you more but time is short. 
                                              
  type \\'ls\\' to see files. use cat to        
display their content.
"""

first_message_raw = """  .-----------------------------------------------------------------.
%-mamamas /  .-.     Hey Dan. You don\\'t know me, but I need your         .-.  \\
%-mamamas|  /   \    help.                                              /   \  |
%-mamamas| |\_.  |   I wish I could tell you more but time is short.   |    /| |
%-mamamas|\|  | /|                                                     |\  | |/|
%-mamamas| `---\\' |   type \\'ls\\' to see files. use cat to                | `---\\' |
%-mamamas|       |   display their content.                            |       | 
%-mamamas|       |-----------------------------------------------------|       |
%-mamamas\       |                                                     |       /
%-mamamas \     /                                                       \     /
%-mamamas  `---\\'                                                         `---\\'"""

first_message = """  .-----------------------------------------------------------------.
 /  .-.     Hey Dan. You don\\'t know me, but I need your         .-.  \\
|  /   \    help.                                              /   \  |
| |\_.  |   I wish I could tell you more but time is short.   |    /| |
|\|  | /|                                                     |\  | |/|
| `---\\' |   type \\'ls\\' to see files. use cat to                | `---\\' |
|       |   display their content.                            |       | 
|       |-----------------------------------------------------|       |
\       |                                                     |       /
 \     /                                                       \     /
  `---\\'                                                         `---\\'"""
# first_message = first_message_raw.replace('mamama', '50')



#### ascii progress bar at the top

## use tput cols and tput lines to render 
## use tput cup x y - see how it works 