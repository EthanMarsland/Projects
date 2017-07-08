# Date Project Created 06/07/2017, D/M/Y
# This sample code is apart of the project "Dice Poker"
# This code is for presentation purposes only

# Owner: Ethan Marsland
# Email: emarsland1214@gmail.com

from tkinter import *
import random

class die:
    def __init__(self):
        # int, number of the die
        self.number = random.randint(1,6)
        
    def roll(self):
        self.number = random.randint(1,6) 
    
class player:

    def countDice(self):
        # loop through and count the dice
        countedDice = [0,0,0,0,0,0]
        i = 0
        while (i < 5):
            if(self.dice[i].number == 1):
                countedDice[0] += 1                
            elif(self.dice[i].number == 2):
                countedDice[1] += 1                
            elif(self.dice[i].number == 3):
                countedDice[2] += 1        
            elif(self.dice[i].number == 4):
                countedDice[3] += 1                
            elif(self.dice[i].number == 5):
                countedDice[4] += 1                
            elif(self.dice[i].number == 6):
                countedDice[5] += 1
            i += 1
        return countedDice
    
    def rollDie(self,dieToRoll):
        self.dice[dieToRoll].roll()

    def rollAllDice(self):
        i = 0
        while i < 5:
            self.rollDie(i)
            i = i + 1    
        
    def __GenerateDice(self):
        i = 0
        while i != 5:
            self.dice.insert(i, die())
            i = i + 1

    def reRollSelectedDice(self):
        i = 0
        while i != 5:
            if(self.selectedDice[i].get() == 1):
                self.rollDie(i)
                self.selectedDice[i].set(0)
            i = i + 1
                
    def __init__(self):
        # intvar, which dice the player wants to swap
        self.selectedDice = []
        i = 0
        while i < 5:
            self.selectedDice.insert(i, IntVar())
            self.selectedDice[i].set(0)
            i += 1
        
        # list, the players dice
        self.dice = []
        # int, how many rounds the player has won
        self.score = 0
        
        self.__GenerateDice()

