import re
from strings import progressBar, first_message
from utils import removeNewLine
from renderer import saveCursorPosition, restoreCursorPosition, goto, printMessage, printMessageAt

class Message():
    @staticmethod
    def createDeleteMessage(message, x):
        split_message = removeNewLine(message).split("\n")
        erased_split_message = [re.sub(r'.', " ", msg) for msg in split_message]
        base = "\n%-mamas".replace("mama", str(x))
        return base.join(erased_split_message)
    @staticmethod
    def createMessage(message, x):        
        split_message = removeNewLine(message).split("\n")
        base = "\n%-mamas".replace("mama", str(x))
        return base.join(split_message)
    def __init__(self, message, id, startPosition):
        self.id = id
        self.message = self.createMessage(message, startPosition[0])
        self.deleteMessage = self.createDeleteMessage(message, startPosition[0])
        self.startPosition = startPosition
    def write(self):
        printMessageAt(self.message, self.startPosition)
    def erase(self):
        # print repr(self.deleteMessage)
        printMessageAt(self.deleteMessage, (self.startPosition[0],self.startPosition[1]-1) )
        


progressBar = Message(progressBar, "prg_bar", (52, 10))
level1_firstMessage = Message(first_message, "lvl1", (50, 11))