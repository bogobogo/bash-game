import re
from strings import progressBar, first_message, totalxp
from consts import IN_WIDTH
from utils import removeNewLine
from renderer import saveCursorPosition, restoreCursorPosition, historyCoversScreen, goto, printMessage, write, printMessageAt, combineHistoryAndMessage, getTerminalSize

class Message():
    @staticmethod
    def createDeleteMessage(message, x):
        split_message = removeNewLine(message).split("\n")
        erased_split_message = [re.sub(r'.', " ", msg) for msg in split_message]
        return erased_split_message
    @staticmethod
    def createMessage(message, x):        
        split_message = removeNewLine(message).split("\n")
        return split_message
    def __init__(self, message, id, startPosition):
        self.id = id
        self.message = self.createMessage(message, startPosition[0])
        self.rawMessage = message
        self.deleteMessage = self.createDeleteMessage(message, startPosition[0])
        self.startPosition = startPosition
        self.x = startPosition[0]
        self.y = startPosition[1]
    def write(self):
        if len(self.message) == 1:
            printMessageAt(self.message[0], self.startPosition)
        printMessageAt(self.message, self.startPosition)
    def erase(self):
        printMessageAt(self.deleteMessage, (self.x, self.y-1) )
    def overlay(self, line_history):
        _ , screen_height = getTerminalSize()
        y = self.y
        if historyCoversScreen(line_history, screen_height):
            y = y-1
        if len(self.message) == 1:
            printMessageAt(self.message[0], (self.x, y))    
        else:
            combinedMessage = combineHistoryAndMessage(self.message, self.y, line_history, screen_height)
            printMessageAt(combinedMessage, (self.x, y))
    def clean(self, line_history):
        _ , screen_height = getTerminalSize()
        y = self.y
        if historyCoversScreen(line_history, screen_height):
            y = y-2
            if len(self.deleteMessage) == 1:
                printMessageAt(self.deleteMessage[0], (self.x, y))
                return
            combinedMessage = combineHistoryAndMessage(self.deleteMessage, y + 1 , line_history, screen_height)
            printMessageAt(combinedMessage, (self.x, y))
            return
        if len(self.deleteMessage) == 1:
            printMessageAt(self.deleteMessage[0], (self.x, y)) 
        else:
            combinedMessage = combineHistoryAndMessage(self.deleteMessage, y , line_history, screen_height)
            printMessageAt(combinedMessage, (self.x, y))
            

        

totalxp = Message(totalxp, "xp message", (IN_WIDTH + 28, 9))
progressBar = Message(progressBar, "prg_bar", (IN_WIDTH + 2, 10))
level1_firstMessage = Message(first_message, "lvl1", (IN_WIDTH + 0, 11))