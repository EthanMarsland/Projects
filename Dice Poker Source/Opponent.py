# Date Project Created 07/07/2017, D/M/Y
# This sample code is apart of the project "Dice Poker"
# This code is for presentation purposes only

# Owner: Ethan Marsland
# Email: emarsland1214@gmail.com
from Player import *

class opponent(player):

    def reRollDice(self):
        # count dice
        countedDice = self.countDice()
        
        # go through the dice and reroll the singles
        i = 0
        # go through the numbers a die can be
        while (i < 6):
            if(countedDice[i] == 1):
                k = 0
                # go through the players dice and swap the single
                while (k < 5):
                    if(self.dice[k].number == i + 1):
                        self.rollDie(k)
                    k += 1
            i += 1
