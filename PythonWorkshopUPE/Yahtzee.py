import Dice

class Yahtzee:
    def __init__(self, inter):
        self.d = Dice.Dice()        # Dice
        self.money = 100            # Money
        self.interface = inter      # Interface (TUI or GUI)

    def playgame(self):
        while (self.interface.playOn()):
            self.d.rollAll()    # Roll all dice
            self.money -= 10    # Placed their bet
            self.interface.showMoney(self.money)    # Show user their money

            for i in range(3):
                self.interface.showDice(self.d.dice)    # Show user their dice
                reroll = self.interface.pickDice()      # Allow user to choose dice
                self.d.roll(reroll)                     # Reroll those dice
                if (len(reroll) == 0):                  # In case I don't want to reroll, break out
                    break

            msg, s = self.d.score()                     # Computing the score
            self.interface.showResult(msg, s)           # Showing the score

            self.money += s                             # Gives player their winnings
            self.interface.showMoney                    # Show money again

        self.interface.close()                          # Close the window

i = TUI.TUI()   # Textual Interface
y = Yahtzee(i)  # Yahtzee Game
y.playgame()    # Play the game