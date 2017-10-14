class TUI:
    def showMoney(self, amt):
        print("You have $", amt)

    def showDice(self, dice):
         print("Your dice are: ", dice)

    def playOn(self):
        print("do you want to play (Y/N)?")
        x = input()
        return (x == "Y")

    def close(self):
        print("Thank you for playing!")

    def showResult(self, msg, score):
        print(msg, "Your score is ", score)

    def pickDice(self):
        print("Which dice do you want to reroll?")
        mydice = input()
        return mydice

