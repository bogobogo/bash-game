import unittest 
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.consts import IN_WIDTH
from src.renderer import getRelevantHistoryLines, combineHistoryAndMessage
from src.messages import Message
from test_strings import first_message_no_tabs

class RendererTest(unittest.TestCase):
    def test_get_corrasponding_lines_with_long_line_history(self):
        line_history = ["hello" for _ in xrange(1, 100)]
        message_lines = first_message_no_tabs.split("\n")
        screen_height = 50
        msg_len = len(message_lines)
        start_position_from_top = 11
        result = getRelevantHistoryLines(line_history, screen_height, msg_len, start_position_from_top)
        self.assertEqual(len(result), len(message_lines) - 1)
        self.assertEqual(result, ["hello" for _ in xrange(0, len(message_lines) - 1)])

    def test_combine_message_and_history_that_covers_the_screen(self):
        line_history = [str(i) + (" " * (IN_WIDTH - len(str(i)))) for i in xrange(1, 100)]
        msg = Message("yo\n"*29 + "yo", "first", (50, 11)) 
        screen_height = 50
        result = combineHistoryAndMessage(msg.message, 11, line_history, screen_height)
        expectedResult = "yo\n" + ((" " * IN_WIDTH) + "yo\n") * 28 + (" " * IN_WIDTH) +  "yo"
        self.assertEqual(result, expectedResult)
    def test_combine_message_and_history_that_intersects(self):
        line_history = ["hello" + (IN_WIDTH - len("hello")) * " " for _ in xrange(0, 15)]
        msg = Message("yo\n"*29 + "yo", "first", (50, 11)) 
        screen_height = 50
        result = combineHistoryAndMessage(msg.message, 11, line_history, screen_height)
        expectedResult = "yo\n" + ("hello" + " " * (IN_WIDTH - len("hello")) + "yo\n") * 4 + (" " * IN_WIDTH  + "yo\n") * 24 + " "*IN_WIDTH + "yo"
        self.assertEqual(result, expectedResult)
    def test_combine_message_and_history_that_doesnt_intersect(self):
        line_history = ["hello"+ " " * 3 for _ in xrange(1, 9)]
        msg = Message("yo\n"*29 + "yo", "first", (50, 11)) 
        screen_height = 50
        result = combineHistoryAndMessage(msg.message, 11, line_history, screen_height)
        expectedResult = "yo\n" + 28* (IN_WIDTH*" " + "yo\n") + " "*IN_WIDTH + "yo"
        self.assertEqual(result, expectedResult)    
    def test_combine_delete_message_and_history(self):
        pass
if __name__ == '__main__':
    unittest.main()