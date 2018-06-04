import unittest 
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.messages import Message
from test_strings import first_message_no_tabs, first_message


class MessagesTest(unittest.TestCase):
    def test_creates_message(self):
        new_message = Message("hello", "111", (0,0))
        self.assertEqual(new_message.message, "hello")
        self.assertEqual(new_message.id, "111", (0,0))
    def test_creates_message_with_new_lines(self):
        new_message = Message(first_message_no_tabs, "111", (50,20))
        self.assertEqual(new_message.message, first_message)  
    def test_deletes_message(self):
        new_message = Message("hello", "111", (0,0))
        self.assertEqual(new_message.deleteMessage, "     ")
    # def test_delete_message_with_new_lines(self):
    #     new_message = Message("hello\n", "111", (0,0))
    #     self.assertEqual(new_message.deleteMessage, "     \n")
    

if __name__ == '__main__':
    unittest.main()