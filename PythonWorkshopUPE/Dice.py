#from random import *
import random

class Dice:
    # Constructor
    def __init__(self):
        self.dice = [0]*5   # Array of five zeroes
        self.rollAll()

    # Roll a set of dice
    def roll(self, which):
        for element in which:
            self.dice[element] = random.randint(1,6)

    # Roll all dice
    def rollAll(self):
        self.roll(range(5))

    def score(self):
        counts = [0]*7      # We'll only use counts[1] to counts[6]
        for i in range(1,6):
            counts[i] = self.dice.count(i)
        if (5 in counts):
            return "5 of a kind", 30
        elif (4 in counts):
            return "4 of a kind", 15
        elif (3 in counts and 2 in counts):
            return "Full house", 12
        elif (3 in counts):
            return "Three of a kind", 10
        elif (counts.count(2) == 2):
            return "Two pair", 5
        elif (2 in counts):
            return "One pair", 2
        else:
            return "Nothing", 0