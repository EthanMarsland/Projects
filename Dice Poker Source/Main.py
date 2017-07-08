# Date Project Created 06/07/2017, D/M/Y
# This sample code is apart of the project "Dice Poker"
# This code is for presentation purposes only

# Owner: Ethan Marsland
# Email: emarsland1214@gmail.com

#! /usr/bin/env python3
import random, pickle
from tkinter import *
from tkinter import messagebox

from Game import *

MAINGUI = Tk() # stores gui into variable

#GameGUI
def startGame():
    # our game controller
    gameController = game()
    
    GAMEGUI = Toplevel()
      
    GAMEGUI.geometry('1200x500')#sets size for window
    GAMEGUI.title("Poker Dice")#sets title
    #Titlelabel = Label(text = "Poker Dice").grid(row = 0, column = 0, sticky = W)#makes label, .grid is for position

    # player one
    p1Dicelabel = Label(GAMEGUI,text = "Player One's Dice:").place(x = 200, y = 150)
    p1DiceListlabel = Label(GAMEGUI,text = str(gameController.playerOne.dice[0].number)).place(x = 310, y = 150)
    
    Label(GAMEGUI,text = str(gameController.playerOne.dice[0].number)).place(x = 310, y = 150)        
    Label(GAMEGUI,text = str(gameController.playerOne.dice[1].number)).place(x = 330, y = 150)
    Label(GAMEGUI,text = str(gameController.playerOne.dice[2].number)).place(x = 350, y = 150)
    Label(GAMEGUI,text = str(gameController.playerOne.dice[3].number)).place(x = 370, y = 150)
    Label(GAMEGUI,text = str(gameController.playerOne.dice[4].number)).place(x = 390, y = 150)

    # player two
    p2Dicelabel = Label(GAMEGUI,text = "Player Two's Dice:").place(x = 200, y = 250)
    p12DiceListlabel = Label(GAMEGUI,text = str(gameController.playerTwo.dice[0].number)).place(x = 310, y = 250)

    Label(GAMEGUI,text = str(gameController.playerTwo.dice[0].number)).place(x = 310, y = 250)
    Label(GAMEGUI,text = str(gameController.playerTwo.dice[1].number)).place(x = 330, y = 250)
    Label(GAMEGUI,text = str(gameController.playerTwo.dice[2].number)).place(x = 350, y = 250)
    Label(GAMEGUI,text = str(gameController.playerTwo.dice[3].number)).place(x = 370, y = 250)
    Label(GAMEGUI,text = str(gameController.playerTwo.dice[4].number)).place(x = 390, y = 250)

    Roundslabel = Label(GAMEGUI, text = "Current Round:").place(x = 0, y = 20)
    currentroundlabel = Label(GAMEGUI, text = str(gameController.round)).place(x = 110, y = 20)
    
    p1scorelabel = Label(GAMEGUI, text = "Player One's Score:").place(x = 0, y = 60)
    currentp1scorelabel = Label(GAMEGUI, text = str(0)).place(x = 110, y = 60)
    
    p2scorelabel = Label(GAMEGUI, text = "Player Two's Score:").place(x = 0, y = 100)
    currentp2scorelabel = Label(GAMEGUI, text = str(0)).place(x = 110, y = 100)

    QuitButton = Button(GAMEGUI,text = "Quit", command = MAINGUI.destroy).place(x = 1148, y = 0)       

    gameController.startGame(GAMEGUI)

#ScoresGUI
def Scores():
    try:
        input_file = open('PokerDiceScores.dat', 'rb')
        scores = pickle.load(input_file)
        scores
    except:
        scores = [0,0,0]
        output_file = open('PokerDiceScores.dat', 'wb')
        pickle.dump(scores, output_file)
        output_file.close()

        
    SCORESGUI = Toplevel()

    SCORESGUI.geometry('500x250')
    SCORESGUI.title("Poker Dice")

    Label(SCORESGUI, text = "Games Won: ").place(x = 50, y = 50)
    Label(SCORESGUI, text = "Games Lost: ").place(x = 50, y = 100)
    Label(SCORESGUI, text = "Games Tied: ").place(x = 50, y = 150)
    
    Label(SCORESGUI, text = scores[0]).place(x = 200, y = 50)
    Label(SCORESGUI, text = scores[1]).place(x = 200, y = 100)
    Label(SCORESGUI, text = scores[2]).place(x = 200, y = 150)
    
    Button(SCORESGUI,text = "Quit", command = MAINGUI.destroy).place(x = 448, y = 0)
    Button(SCORESGUI,text = "Close", command = SCORESGUI.destroy).place(x = 448, y = 170)
    
    
#Rules GUI
def Rules():
    # define gui
    RULESGUI = Toplevel()
    RULESGUI.geometry('700x500')
    RULESGUI.title("Poker Dice")
    # labels
    Label(RULESGUI, text = "Rules of Dice Poker:").place(x = 25, y = 50)
    Label(RULESGUI, text = "The aim of dice poker is to get a superior combination compared to your opponent.").place(x = 45, y = 70)
    Label(RULESGUI, text = "There are 6 combinations, from highest to lowest:").place(x = 65, y = 90)
    Label(RULESGUI, text = "Five of a kind: Five dice showing the same value").place(x = 75, y = 110)
    Label(RULESGUI, text = "Four of a kind: Four dice showing the same value").place(x = 75, y = 130)
    Label(RULESGUI, text = "Full House: A pair and a three of a kind").place(x = 75, y = 150)
    Label(RULESGUI, text = "Three of a kind: Three dice showing the same value").place(x = 75, y = 170)
    Label(RULESGUI, text = "Two pairs: dice showing two matched pairs of values").place(x = 75, y = 190)
    Label(RULESGUI, text = "One pair: dice showing a single matched pair of values").place(x = 75, y = 210)
    
    Label(RULESGUI, text = "How to play:").place(x = 25, y = 300)
    Label(RULESGUI, text = "Each Player rolls their dice then chooses which dice they wish to reroll").place(x = 45, y = 320)
    Label(RULESGUI, text = "The player with the superiour combination wins the round").place(x = 45, y = 340)
    Label(RULESGUI, text = "The winner is whoever wins 3 times. If it is a tie then a 4th round is played as tiebreaker" ).place(x = 45, y = 360)

 # buttons
    Button(RULESGUI,text = "Quit", command = MAINGUI.destroy).place(x = 648, y = 0)
    Button(RULESGUI,text = "Close", command = RULESGUI.destroy).place(x = 648, y = 400)

#MainGUI
MAINGUI.geometry('300x100')
MAINGUI.title("Dice Poker")

Button(MAINGUI, text = "New Game", command = startGame).place(x = 20,y = 50)
Button(MAINGUI, text = "Scores", command = Scores).place(x = 125, y = 50)
Button(MAINGUI,text = "Quit", command = MAINGUI.destroy).place(x = 266, y = 0)
Button(MAINGUI, text = "Rules", command = Rules).place(x = 200, y = 50)
MAINGUI.mainloop()
