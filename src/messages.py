import re
from strings import progressBar, first_message
from utils import removeNewLine
from renderer import saveCursorPosition, restoreCursorPosition, goto, printMessage, printMessageAt

class Message():
    @staticmethod
    def createDeleteMessage(message, x):
        split_message = removeNewLine(message).split("\n")
        erased_split_message = [re.sub(r'.', " ", msg) for msg in split_message]
        return era
    @staticmethod
    def createMessage(message, x):        
        split_message = removeNewLine(message).split("\n")
        return split_message
    def __init__(self, message, id, startPosition):
        self.id = id
        self.message = self.createMessage(message, startPosition[0])
        self.deleteMessage = self.createDeleteMessage(message, startPosition[0])
        self.startPosition = startPosition
    def write(self):
        for idx, line in enumerate(self.message):
            printMessageAt(line, (self.startPosition[0], self.startPosition[1] + idx )) 
        
    def erase(self):
        for idx, line in enumerate(self.deleteMessage):
            printMessageAt(line, (self.startPosition[0], self.startPosition[1] + idx )) 
        


progressBar = Message(progressBar, "prg_bar", (52, 10))
level1_firstMessage = Message(first_message, "lvl1", (50, 11))