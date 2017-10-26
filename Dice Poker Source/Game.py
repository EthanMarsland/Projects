# Date Project Created 06/07/2017, D/M/Y
# This sample code is apart of the project "Dice Poker"
# This code is for presentation purposes only

# Owner: Ethan Marsland
# Email: ethan.marsland17@gmail.com

import pickle
from enum import Enum
from enum import IntEnum

from tkinter import *
from tkinter import messagebox

from Player import *
from Opponent import *

# enum for each stage of the game
class GameStage(Enum):
    PlayerOneRoll, PlayerTwoRoll,PlayerOneReRoll,PlayerTwoReRoll,CheckWinner = range(5)

# enum for each combination of the game
# normal Enums cannot be compared, but subclass IntEnums can
class DiceCombination(IntEnum):
    Nothing,Pair,TwoPairs,ThreeKind,FiveStraight,SixStraight,FullHouse,FourKind,FiveKind = range(9)

class game:
    def __init__(self):
        # int, which round of the game we're playing
        self.round = 1
        # player, first player
        self.playerOne = player()
        # player, second player
        self.playerTwo = opponent()
        # enum, so we know which stage of the game we are playing
        self.__stage = GameStage.PlayerOneRoll

    ### start saveScores
    ### old code will rewrite later
    def __saveScores(self, winner):
        try:
            input_file = open('PokerDiceScores.dat', 'rb')#opens file
            scores = pickle.load(input_file)#loads data into variable
            scores#don't know what this is for was there when I read the book for last project
            if winner == 1:
                scores[0] = scores[0] + 1
                output_file = open('PokerDiceScores.dat', 'wb')
                pickle.dump(scores, output_file)#dumps data
                output_file.close()#closes file
            elif winner == 2:
                scores[1] = scores[1] + 1
                output_file = open('PokerDiceScores.dat', 'wb')
                pickle.dump(scores, output_file)
                output_file.close()  
            elif winner == 0:
                scores[2] = scores[2] + 1
                output_file = open('PokerDiceScores.dat', 'wb')
                pickle.dump(scores, output_file)
                output_file.close()
        except:#incase there isn't a data file
            scores = [0,0,0]
            if winner == 1:
                scores[0] = scores[0] + 1
                output_file = open('PokerDiceScores.dat', 'wb')#opens file
                pickle.dump(scores, output_file)#dumps data
                output_file.close()#closes file
            elif winner == 2:
                scores[1] = scores[1] + 1
                output_file = open('PokerDiceScores.dat', 'wb')
                pickle.dump(scores, output_file)
                output_file.close()  
            elif winner == 0:
                scores[2] = scores[2] + 1
                output_file = open('PokerDiceScores.dat', 'wb')
                pickle.dump(scores, output_file)
                output_file.close()
    ### end saveScores
                
    def __checkPlayerCombination(self, playerDice):
        # five straight
        if(playerDice[0] == 1 and playerDice[1] == 2 and playerDice[2] == 3
           and playerDice[3] == 4 and playerDice[4] == 5):
            return DiceCombination.FiveStraight
        # six straight
        if(playerDice[0] == 2 and playerDice[1] == 3 and playerDice[2] == 4
           and playerDice[3] == 5 and playerDice[4] == 6):
            return DiceCombination.SixStraight        
        pair = 0
        threekind = 0
        i = 0
        while(i < 6):
            # best combination lets just return here
            if playerDice[i] == 5:
                return DiceCombination.FiveKind
            # second best combination
            if playerDice[i] == 4:
                return DiceCombination.FourKind
            # threekind, still could be a pair for a full house
            if playerDice[i] == 3:
                threekind += 1
            # pair, we can have two of these or a full house
            if playerDice[i] == 2:
                pair += 1
            i += 1
        if(pair == 0):
            if(threekind == 1):
                return DiceCombination.ThreeKind
        if (pair == 1):
            if(threekind == 1):
                return DiceCombination.FullHouse
            elif(threekind == 0):
                return DiceCombination.Pair
        if (pair == 2):
            return DiceCombination.TwoPairs

        # we got no combination
        return DiceCombination.Nothing                                
    
    def __checkWinner(self):
        # count dice
        playerOneDice = self.playerOne.countDice()
        playerTwoDice = self.playerTwo.countDice()
        # check players combinations
        playerOneCombination = self.__checkPlayerCombination(playerOneDice)
        playerTwoCombination = self.__checkPlayerCombination(playerTwoDice)
        # find winner
        # player one wins
        if(playerOneCombination > playerTwoCombination):
            return 1
        # player 2 wins
        elif(playerTwoCombination > playerOneCombination):
            return 2
        # players tie
        elif(playerOneCombination == playerTwoCombination):
            return 0

    def displayDice(self, gameGUI, playerVar, Y):
        
        Label(gameGUI,text = str(playerVar.dice[0].number)).place(x = 310, y = Y)        
        Label(gameGUI,text = str(playerVar.dice[1].number)).place(x = 330, y = Y)
        Label(gameGUI,text = str(playerVar.dice[2].number)).place(x = 350, y = Y)
        Label(gameGUI,text = str(playerVar.dice[3].number)).place(x = 370, y = Y)
        Label(gameGUI,text = str(playerVar.dice[4].number)).place(x = 390, y = Y)

    def displayScores(self, gameGUI):
        Label(gameGUI, text = str(self.round)).place(x = 110, y = 20)
        Label(gameGUI, text = str(self.playerOne.score)).place(x = 110, y = 60)
        Label(gameGUI, text = str(self.playerTwo.score)).place(x = 110, y = 100)
        
    def __diceToReRoll(self, gameGUI, playerVar):
        Checkbutton(gameGUI, text = "Die 1", variable = playerVar.selectedDice[0],
                    onvalue = 1, offvalue = 0).place(x = 570, y = 200)
        Checkbutton(gameGUI, text = "Die 2", variable = playerVar.selectedDice[1],
                    onvalue = 1, offvalue = 0).place(x = 620, y = 200)
        Checkbutton(gameGUI, text = "Die 3", variable = playerVar.selectedDice[2],
                    onvalue = 1, offvalue = 0).place(x = 670, y = 200)
        Checkbutton(gameGUI, text = "Die 4", variable = playerVar.selectedDice[3],
                    onvalue = 1, offvalue = 0).place(x = 720, y = 200)
        Checkbutton(gameGUI, text = "Die 5", variable = playerVar.selectedDice[4],
                    onvalue = 1, offvalue = 0).place(x = 770, y = 200)

    def __continue(self, gameGUI):
        # player one roll
        if(self.__stage is GameStage.PlayerOneRoll):
            
            self.playerOne.rollAllDice()
            self.displayDice(gameGUI, self.playerOne, 150)
            
            self.__stage = GameStage.PlayerTwoRoll
            messagebox.showinfo("Dice Poker", "Player Twos turn to roll their dice")

        # player two roll    
        elif(self.__stage is GameStage.PlayerTwoRoll):
            self.playerTwo.rollAllDice()
            
            self.displayDice(gameGUI, self.playerTwo, 250)

            self.__stage = GameStage.PlayerOneReRoll
            messagebox.showinfo("Dice Poker", "Player Ones turn to reroll their dice")
            
            self.__diceToReRoll(gameGUI, self.playerOne)
            
        # player one reroll    
        elif(self.__stage is GameStage.PlayerOneReRoll):
            self.playerOne.reRollSelectedDice()

            self.displayDice(gameGUI, self.playerOne, 150)

            self.__stage = GameStage.PlayerTwoReRoll
            messagebox.showinfo("Dice Poker", "Player twos turn to reroll their dice")

        # player two reroll
        elif(self.__stage is GameStage.PlayerTwoReRoll):
            self.playerTwo.reRollDice()
            self.displayDice(gameGUI, self.playerTwo, 250)

            self.__stage = GameStage.CheckWinner
            messagebox.showinfo("Dice Poker", " Time to check winner")
            
        # check winner
        elif(self.__stage is GameStage.CheckWinner):
            
            winner = self.__checkWinner()
            
            if(winner == 0):
                self.playerOne.score += 1
                self.playerTwo.score += 1
                messagebox.showinfo("Dice Poker", "Players have tied!")
            elif(winner == 1):
                self.playerOne.score += 1
                messagebox.showinfo("Dice Poker", "Player Ones Wins!")
            elif(winner == 2):
                self.playerTwo.score += 1
                messagebox.showinfo("Dice Poker", "Player Two Wins!")
                
            self.round += 1
            
            # end of match
            if(self.round == 4):
                if(self.playerOne.score == 3):
                    messagebox.showinfo("Dice Poker", "Player One wins the match!")
                    self.__saveScores(1)
                if(self.playerTwo.score == 3):
                    messagebox.showinfo("Dice Poker", "Player Two wins the match!")
                    self.__saveScores(2)
                if(self.playerOne.score == 2 and self.playerTwo.score == 2):
                    messagebox.showinfo("Dice Poker", "Players have tied the match!")
                    self.__saveScores(0)
                # restart
                self.playerOne.score = 0
                self.playerTwo.score = 0
                self.round = 0
                
            self.displayScores(gameGUI)
            
            self.__stage = GameStage.PlayerOneRoll
            messagebox.showinfo("Dice Poker", "Player Ones turn to roll their dice")
            
    def startGame(self, gameGUI):        
        messagebox.showinfo("Dice Poker", "Player Ones turn to roll their dice")
            
        Button(
            gameGUI,text = "Continue",
            command = lambda: self.__continue(gameGUI)).place(x = 1000, y = 400)
