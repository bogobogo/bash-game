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

first_message_no_tabs = """  .-----------------------------------------------------------------.
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
first_message = first_message_raw.replace('mamama', '50')