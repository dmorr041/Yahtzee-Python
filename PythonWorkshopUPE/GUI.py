from graphics import *

class GUI:
    def __init__(self):
        self.win = GraphWin("YAHTZEE", 500, 500)

    def close(self):
        self.win.close()

    def showMoney(self,amt):
        # Put the point in the center of the window
        txt = Text(Point(250,250), "You have $" + str(amt))     # Must type cast to concatenate a string and int
        txt.draw(self.win)

    def playOn(self):
        button = Rectangle(Point(200,300), Point(300,400))
        button.draw(self.win)
        point = self.win.getMouse()
        if (point.x >= 200 and point.x <= 300 and point.y >= 300 and point.y <= 400):
            return True
        else:
            return False

