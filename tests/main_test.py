import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import addOutput, fill_line, render_totalout, addUserInput, prompt, InvalidArgument 


class Tests(unittest.TestCase):
    ls_output = 'ideas.py\nmain.py\ntest.py\nutils.py\n'
    ps_putput = '  PID TTY           TIME CMD\n 1366 ttys000    0:00.21 /bin/zsh -l\n 1743 ttys000    0:00.03 python\n  534 ttys001    0:00.02 python\n81324 ttys001    0:00.03 /Applications/iTerm.app/Contents/MacOS/iTerm2 --server login -fp eladbo\n81326 ttys001    0:00.54 -zsh\n 1756 ttys002    0:00.44 -zsh\n 4082 ttys002    0:00.03 /usr/bin/python ./main.py\n'
    def test_fill_line(self):
        l = 'asdf'
        c = '.'
        in_width = 80
        expected = 'asdf' + ('.' * (in_width-len(l)))
        result = fill_line(l, c, in_width=in_width)
        self.assertEqual(expected, result)

    def test_fill_line_invalid_char(self):
        l = 'asdf'
        c = '..'
        in_width = 80
        expected = 'asdf' + ('.' * (in_width-len(l)))
        self.assertRaises(
            InvalidArgument,
            lambda: fill_line(l, c, in_width=in_width)
        )

    def test_addOutput_1_line(self):
        output = 'ideas.py\n'
        totalout_lines = []
        result = [
            fill_line('ideas.py','.'),
        ]
        addOutput(output, totalout_lines)
        self.assertEqual(totalout_lines, result)

    def test_addOutput_ls(self):
        totalout_lines = []
        result = [
            fill_line('ideas.py','.'),
            fill_line('main.py','.'),
            fill_line('test.py','.'),
            fill_line('utils.py','.'),
        ]
        addOutput(self.ls_output, totalout_lines, in_width=80)
        self.assertEqual(totalout_lines, result)

    def test_addOutput_over_IN_WIDTH(self):
        totalout_lines = []
        result = [
            fill_line('ideas.py','.'),
            fill_line('main.py','.'),
            fill_line('test.py','.'),
            fill_line('utils.py','.'),
        ]
        addOutput(self.ls_output, totalout_lines)
        self.assertEqual(totalout_lines, result)
    def test_add_user_input_fill(self):
        cmd = "top -a"
        totalout_lines = [
            prompt + "ls",
            fill_line('main.py',c = '.'),
            prompt
         ]
        addUserInput(cmd, totalout_lines)
        expected = [
            prompt + "ls",
            fill_line('main.py',c = '.'),
            fill_line(prompt + cmd, c = '.', compensation=10)
         ]
        self.assertEqual(totalout_lines, expected)
        
if __name__ == '__main__':
    unittest.main()