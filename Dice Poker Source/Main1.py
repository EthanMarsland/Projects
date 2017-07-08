# Year Created 2015
# This sample code is apart of the project "Dice Poker"
# This code is for presentation purposes only

# Owner: Ethan Marsland
# Email: emarsland1214@gmail.com

#! /usr/bin/env python3
import random, pickle#random module for random numbers and pickle module for inputing and outputing data from files
from tkinter import *#module for GUI
from tkinter import messagebox#module for messageboxes

# import player file
from Player import *

#all global variables for code
global swapped, playerrolled, playdice, player2dice, rolled, nextvar, AIRolled, rounds, playeronescore,playertwoscore
nextvar = "not rolled"#so the player rolls before the computer
rolled = False#this prevents rolling more than once
playdice = []#player ones dice list
player2dice = []#player twos dice list
nextvar = ""#orginialy commenced the next phase of the game, now ends the game
AIRolled = False#cant remember what for
swapped = False#prevents A.I dice from be swapped multiple times in a row
rounds = 1#three rounds, game starts at one
playeronescore = 0#scores; winner is best of three
playertwoscore = 0
        
def nextround():#checks the scores and rounds to see who has won
    global rounds, nextvar
    if rounds < 3 and nextvar != "game complete":
        rounds = rounds + 1
        resetvars()
    elif rounds == 3:
        if playeronescore == 2 and playertwoscore == 2:
            resetvars()
        elif playeronescore == 0 and playertwoscore == 2 and rounds == 2:
            #message box: messagebox calls module, showinfo is what type of message box (askquestion is for yes or no input which returns string for you)
            #first string is title of messagebox, next is the info
            WINNERmessagebox = messagebox.showinfo("Dice Poker", "player two wins match")
            currentroundlabel = Label(GAMEGUI, text = str(rounds)).place(x = 900, y = 50)
            nextvar = "game complete"
            winner = "player two wins match"
            SaveScores(winner)
        elif playertwoscore == 0 and playeronescore == 2 and rounds == 3:
            WINNERmessagebox = messagebox.showinfo("Dice Poker", "player one wins match")
            currentroundlabel = Label(GAMEGUI, text = str(rounds)).place(x = 900, y = 50)
            nextvar = "game complete"
            winner = "player one wins match"
            SaveScores(winner)
        elif playeronescore > playertwoscore and rounds == 3:
            WINNERmessagebox = messagebox.showinfo("Dice Poker", "player one wins match")
            currentroundlabel = Label(GAMEGUI, text = str(rounds)).place(x = 900, y = 50)
            nextvar = "game complete"
            winner = "player one wins match"
            SaveScores(winner)
        elif playeronescore < playertwoscore and rounds == 3 or rounds == 4:
            WINNERmessagebox = messagebox.showinfo("Dice Poker", "player two wins match")
            currentroundlabel = Label(GAMEGUI, text = str(rounds)).place(x = 900, y = 50)
            nextvar = "game complete"
            winner = "player two wins match"
            SaveScores(winner)
        elif playeronescore == playertwoscore and rounds == 3 or rounds == 4:
            WINNERmessagebox = messagebox.showinfo("Dice Poker", "This match is a tie")
            currentroundlabel = Label(GAMEGUI, text = str(rounds)).place(x = 900, y = 50)
            nextvar = "game complete"
            winner = "match ends in tie"
            SaveScores(winner)
    
def resetvars():#resets variables required for the game to progess and increments round
    global playerrolled, playdice, player2dice, rolled, nextvar, AIRolled, preswapped1,preswapped2,preswapped3,preswapped4,preswapped5,rounds,swapped    
    swapped = False
    nextvar = "not rolled"#so the player rolls before the computer
    rolled = False#this prevents rolling more than once
    playdice = []#player ones dice list
    player2dice = []#player twos dice list
    AIRolled = False
    rolled = False
    preswapped1 = 0
    preswapped2 = 0
    preswapped3 = 0
    preswapped4 = 0
    preswapped5 = 0
    nextvar = ""
    currentroundlabel = Label(GAMEGUI, text = str(rounds)).place(x = 900, y = 50)
    
#generate dice for player one
def Dice():
    global nextvar, rolled, playdice
    if rolled == False:
        count = 1
        while count != 6:
            dice = random.randint(1,6)
            playdice.insert(count, dice)
            count = count + 1
        
        DiceListlabel = Label(GAMEGUI,text = str(playdice)).place(x = 110, y =50)
        nextvar = "rolled"
        rolled = True
        AIDice()

#generate dice for player two (A.I.)
def AIDice():
    global nextvar, player2dice,AIRolled
    count = 1
    nextvar = 0
    AIRolled = True
    
    while count != 6:
        dice = random.randint(1,6)
        player2dice.insert(count, dice)
        count = count + 1   
    
                  
    DiceListlabel = Label(GAMEGUI,text = str(player2dice)).place(x = 110, y =150)
    
   
#swap dice function
def SwapDice(DiceSwap):#the way this was written makes it useless for other players
    global playdice, nextvar, nextvar
    nextvar = nextvar + 1
    dice = random.randint(1,6)
    del playdice[DiceSwap]
    playdice.insert(DiceSwap, dice)
       


global preswapped1,preswapped2,preswapped3,preswapped4,preswapped5#Variables used to be sure the player doesn't swap more than once
preswapped1 = 0
preswapped2 = 0
preswapped3 = 0 
preswapped4 = 0
preswapped5 = 0

#first dice
def SwapButton1():#these functions are for swapping the dice
    global preswapped1,AIRolled 
    if preswapped1 == 0 and AIRolled == True:
        preswapped1 = 1
        DiceSwap = 0
        SwapDice(DiceSwap)
    else:
        NOTALLOWEDmessagebox = messagebox.showinfo("Dice Poker", "You cannot swap twice")
        
#second dice
def SwapButton2():
    global preswapped2
    if preswapped2 == 0 and AIRolled == True:
        preswapped2 = 1
        DiceSwap = 1
        SwapDice(DiceSwap)
    else:
        NOTALLOWEDmessagebox = messagebox.showinfo("Dice Poker", "You cannot swap twice")
#third dice   
def SwapButton3():
    global preswapped3
    if preswapped3 == 0 and AIRolled == True:
        preswapped3 = 1
        DiceSwap = 2
        SwapDice(DiceSwap)
    else:
        NOTALLOWEDmessagebox = messagebox.showinfo("Dice Poker", "You cannot swap twice")

#fourth dice    
def SwapButton4():
    global preswapped4
    if preswapped4 == 0 and AIRolled == True:
        preswapped4 = 1
        DiceSwap = 3
        SwapDice(DiceSwap)
    else:
        NOTALLOWEDmessagebox = messagebox.showinfo("Dice Poker", "You cannot swap twice")
#fifth dice    
def SwapButton5():
    global preswapped5
    if preswapped5 == 0 and AIRolled == True:
        preswapped5 = 1
        DiceSwap = 4
        SwapDice(DiceSwap)
    else:
        NOTALLOWEDmessagebox = messagebox.showinfo("Dice Poker", "You cannot swap twice")

#new dice appear after this function is called and calls function that swaps A.I. Dice
def swappingcomplete():#When the player doesn't want to swap anymore
    global preswapped1,preswapped2,preswapped3,preswapped4,preswapped5, nextvar, swapped
    if AIRolled == True and nextvar != "game complete" and swapped == False:
        preswapped1 = 1
        preswapped2 = 1
        preswapped3 = 1
        preswapped4 = 1
        preswapped5 = 1
        nextvar = 5
        DiceListlabel1 = Label(GAMEGUI,text = str(playdice)).place(x = 110, y =50)
        swapped = True
        diceswapAI()
    else:
        NOTALLOWEDmessagebox = messagebox.showinfo("Dice Poker", "You cannot swap twice")

#Function for A.I to swap dice; it checks if it has any dice that is on it's own and rerolls it
def diceswapAI():
    #Part One: Sorting dice into variables then an array
    global player2dice

    count = 0
    checkeddice = [0,0,0,0,0,0]

    #loop that sorts dice into an array    
    while count != 5:
        if player2dice[count] == 1:
            checkeddice[0] = checkeddice[0] + 1
            count = count + 1                         
        elif player2dice[count] == 2:
            checkeddice[1] = checkeddice[1] + 1
            count = count + 1
        elif player2dice[count] == 3:
            checkeddice[2] = checkeddice[2] + 1
            count = count + 1
        elif player2dice[count] == 4:
            checkeddice[3] = checkeddice[3] + 1
            count = count + 1
        elif player2dice[count] == 5:
            checkeddice[4] = checkeddice[4] + 1
            count = count + 1
        elif player2dice[count] == 6:
            checkeddice[5] = checkeddice[5] + 1
            count = count + 1
               
    #Part Two: Swapping
    count = 0
    count2 = 0
    dicecount = 0

    #loop replaces die on their own
    while count != 6:
        if checkeddice[dicecount] < 2:            
            while count2 != 5:
                if player2dice[count2] == dicecount:
                    dice = random.randint(1,6)
                    del player2dice[count2]
                    player2dice.insert(count2, dice)
                    count2 = count2 + 1
                else:
                    count2 = count2 + 1
                
        count = count + 1
        count2 = 0
        dicecount = dicecount + 1
                
    DiceListlabel = Label(GAMEGUI,text = str(player2dice)).place(x = 110, y =150)
    
####Dice Check               
def DiceCheck():
    global playdice, player2dice
    dicecount = 0
    count = 0

    #the players dice are sorted into two arrays: player1checkeddice and player2checkeddice
    #each position in these arrays are how many each player have of each dice in their respective index
    player1checkeddice = [0,0,0,0,0,0]
        
    while count != 5:
        if playdice[count] == 1:
            player1checkeddice[0] = player1checkeddice[0] + 1
            count = count + 1                         
        elif playdice[count] == 2:
            player1checkeddice[1] = player1checkeddice[1] + 1
            count = count + 1
        elif playdice[count] == 3:
            player1checkeddice[2] = player1checkeddice[2] + 1
            count = count + 1
        elif playdice[count] == 4:
            player1checkeddice[3] = player1checkeddice[3] + 1
            count = count + 1
        elif playdice[count] == 5:
            player1checkeddice[4] = player1checkeddice[4] + 1
            count = count + 1
        elif playdice[count] == 6:
            player1checkeddice[5] = player1checkeddice[5] + 1
            count = count + 1            

    count = 0
    
    player2checkeddice = [0,0,0,0,0,0]
    
    while count != 5:
        if player2dice[count] == 1:
            player2checkeddice[0] = player2checkeddice[0] + 1
            count = count + 1                         
        elif player2dice[count] == 2:
            player2checkeddice[1] = player2checkeddice[1] + 1
            count = count + 1
        elif player2dice[count] == 3:
            player2checkeddice[2] = player2checkeddice[2] + 1
            count = count + 1
        elif player2dice[count] == 4:
            player2checkeddice[3] = player2checkeddice[3] + 1
            count = count + 1
        elif player2dice[count] == 5:
            player2checkeddice[4] = player2checkeddice[4] + 1
            count = count + 1
        elif player2dice[count] == 6:
            player2checkeddice[5] =player2checkeddice[5] + 1
            count = count + 1
    
            
    #possible combinations for each player
    playonepair = 0
    playonethreekind = 0
    playonefourkind = 0
    playonefivekind = 0

    playtwopair = 0
    playtwothreekind = 0
    playtwofourkind = 0
    playtwofivekind = 0

    dicecount = 0
    count = 0
    #the players are ranked depending on their combination
    #player one
    while count <= 5:
        if player1checkeddice[dicecount] == 2:
            playonepair = playonepair + 1
            count = count + 1
            dicecount = dicecount + 1
        elif player1checkeddice[dicecount] == 3:
            playonethreekind = playonethreekind + 1
            count = count + 1
            dicecount = dicecount + 1
        elif player1checkeddice[dicecount] == 4:
            playonefourkind = playonefourkind + 1
            count = count + 1
            dicecount = dicecount + 1
        elif player1checkeddice[dicecount] == 5:
            playonefivekind = playonefivekind + 1
            count = count + 1
            dicecount = dicecount + 1
        else:
            count = count + 1
            dicecount = dicecount + 1
        

	
    #player two
    count = 0
    dicecount = 0
    while count <= 5:
        if player2checkeddice[dicecount] == 2:
            playtwopair = playtwopair + 1
            count = count + 1
            dicecount = dicecount + 1
        elif player2checkeddice[dicecount] == 3:
            playtwothreekind = playtwothreekind + 1
            count = count + 1
            dicecount = dicecount + 1
        elif player2checkeddice[dicecount] == 4:
            playtwofourkind = playtwofourkind + 1
            count = count + 1
            dicecount = dicecount + 1
        elif player2checkeddice[dicecount] == 5:
            playtwofivekind = playtwofivekind + 1
            count = count + 1
            dicecount = dicecount + 1
        else:
            count = count + 1
            dicecount = dicecount + 1
    ###ranking

    play1rank = 0
    play2rank = 0

    #this goes through what players combinations are and ranks them
    #player one
    
    if playonepair == 1:
        play1rank = 1
    elif playonepair == 2:
        play1rank = 2
    elif playonethreekind == 1:
        if playonepair == 1:
            play1rank == 6
        else:
            play1rank = 3
    elif playonefourkind == 1:
        play1rank = 7
    elif playonefivekind == 1:
        play1rank = 8
    

    #player two
    if playtwopair == 1:
        play2rank = 1
    elif playtwopair == 2:
        play2rank = 2
    elif playtwothreekind == 1:
        if playtwopair == 1:
            play2rank = 6
        else:
            play2rank = 3
    elif playtwofourkind == 1:
        play2rank = 7
    elif playtwofivekind == 1:
        play2rank = 8
    

    
    #comparing ranks
    if play1rank > play2rank:
        winner = "player one"
        win(winner)
    elif play2rank > play1rank:
        winner = "player two"
        win(winner)
    elif play1rank == play2rank:
        tiebreaking(play1rank,play2rank,player1checkeddice,player2checkeddice)
        
#tiebreaking function; hardest, most tedious and worst written code in this software solution. I hope it works worked so hard for this garbage code.      
#function checks ranks to see how the players tied then it gives a new rank based upon dice value
#player with highest rank wins
def tiebreaking(play1rank,play2rank,player1checkeddice,player2checkeddice):
    count = 0
    ####for single pair
    if play1rank == 1 and play2rank == 1:
        while count != 1:
            if player1checkeddice[0] == 2:
                play1tiebreaker = 1
            elif player1checkeddice[1] == 2:
                play1tiebreaker = 2
            elif player1checkeddice[2] == 2:
                play1tiebreaker = 3
            elif player1checkeddice[3] == 2:
                play1tiebreaker = 4
            elif player1checkeddice[4] == 2:
                play1tiebreaker = 5
            elif player1checkeddice[5] == 2:
                play1tiebreaker = 6
            count = 1
        count = 0
        while count != 1:
            if player2checkeddice[0] == 2:
                play2tiebreaker = 1
            elif player2checkeddice[1] == 2:
                play2tiebreaker = 2
            elif player2checkeddice[2] == 2:
                play2tiebreaker = 3
            elif player2checkeddice[3] == 2:
                play2tiebreaker = 4
            elif player2checkeddice[4] == 2:
                play2tiebreaker = 5
            elif player2checkeddice[5] == 2:
                play2tiebreaker = 6
            count = 1
            
    #####for two pairs        
    elif play1rank == 2 and play2rank == 2:
        play1tiebreaker = 0#variables needed due to several possiblities for pairs
        play2tiebreaker = 0
        while count != 1:
            #pair 1
            if player1checkeddice[0] == 2:
                play1tiebreaker = play1tiebreaker + 1
            elif player1checkeddice[0] == 4:#if both pairs are 1s
                play1tiebreaker = play1tiebreaker + 2

            #pair 2
            elif player1checkeddice[1] == 2:
                play1tiebreaker = play1tiebreaker + 2
            elif player1checkeddice[1] == 4:#if both pairs are 2s
                play1tiebreaker = play1tiebreaker + 4

            #pair3
            elif player1checkeddice[2] == 2:
                play1tiebreaker = play1tiebreaker  + 3
            elif player1checkeddice[2] == 4:#if both pairs are 3s
                play1tiebreaker = play1tiebreaker + 6

            #pair4
            elif player1checkeddice[3] == 2:
                 play1tiebreaker = play1tiebreaker + 4
            elif player1checkeddice[3] == 4:#if both pairs are 4s
                play1tiebreaker = play1tiebreaker + 8                    
                    
            #pair5
            elif player1checkeddice[4] == 2:
                play1tiebreaker = play1tiebreaker + 5
            elif player1checkeddice[4] == 4:#if both pairs are 5s
                play1tiebreaker = play1tiebreaker + 10
                    
            #pair 6
            elif player1checkeddice[5] == 2:
                play1tiebreaker = play1tiebreaker + 6
            elif player1checkeddice[5] == 4:#if both pairs are 6s
                play1tiebreaker = play1tiebreaker + 12
            count = count + 1
            
    ####For Threekinds     
    elif play1rank == 3 and play2rank == 3:
        while count != 1:
            if player1checkeddice[0] == 3:
                play1tiebreaker = 1
            elif player1checkeddice[1] == 3:
                play1tiebreaker = 2
            elif player1checkeddice[2] == 3:
                play1tiebreaker = 3
            elif player1checkeddice[3] == 3:
                play1tiebreaker = 4
            elif player1checkeddice[4] == 3:
                play1tiebreaker = 5
            elif player1checkeddice[5] == 3:
                play1tiebreaker = 6
            count = 1
        count = 0
        while count != 1:
            if player2checkeddice[0] == 3:
                play2tiebreaker = 1
            elif player2checkeddice[1] == 3:
                play2tiebreaker = 2
            elif player2checkeddice[2] == 3:
                play2tiebreaker = 3
            elif player2checkeddice[3] == 3:
                play2tiebreaker = 4
            elif player2checkeddice[4] == 3:
                play2tiebreaker = 5
            elif player2checkeddice[5] == 3:
                play2tiebreaker = 6
            count = 1
    ####for fullhouse (threekind and a pair)

    #threekinds
    elif play1rank == 6 and play2rank == 6:
        while count != 1:
            if player1checkeddice[0] == 3:
                play1tiebreaker = 1
            elif player1checkeddice[1] == 3:
                play1tiebreaker = 2
            elif player1checkeddice[2] == 3:
                play1tiebreaker = 3
            elif player1checkeddice[3] == 3:
                play1tiebreaker = 4
            elif player1checkeddice[4] == 3:
                play1tiebreaker = 5
            elif player1checkeddice[5] == 3:
                play1tiebreaker = 6
            count = 1
        count = 0
        while count != 1:
            if player2checkeddice[0] == 3:
                play2tiebreaker = 1
            elif player2checkeddice[1] == 3:
                play2tiebreaker = 2
            elif player2checkeddice[2] == 3:
                play2tiebreaker = 3
            elif player2checkeddice[3] == 3:
                play2tiebreaker = 4
            elif player2checkeddice[4] == 3:
                play2tiebreaker = 5
            elif player2checkeddice[5] == 3:
                play2tiebreaker = 6
            count = 1
    #single pair
        count = 0
        while count != 1:
            if player1checkeddice[0] == 2:
                play1tiebreaker = play1tiebreaker + 1
            elif player1checkeddice[1] == 2:
                play1tiebreaker = play1tiebreaker + 2
            elif player1checkeddice[2] == 2:
                play1tiebreaker = play1tiebreaker + 3
            elif player1checkeddice[3] == 2:
                play1tiebreaker = play1tiebreaker + 4
            elif player1checkeddice[4] == 2:
                play1tiebreaker = play1tiebreaker + 5
            elif player1checkeddice[5] == 2:
                play1tiebreaker = play1tiebreaker + 6
            count = 1
        count = 0
        while count != 1:
            if player2checkeddice[0] == 2:
                play2tiebreaker = play2tiebreaker + 1
            elif player2checkeddice[1] == 2:
                play2tiebreaker = play2tiebreaker + 2
            elif player2checkeddice[2] == 2:
                play2tiebreaker = play2tiebreaker + 3
            elif player2checkeddice[3] == 2:
                play2tiebreaker = play2tiebreaker + 4
            elif player2checkeddice[4] == 2:
                play2tiebreaker = play2tiebreaker + 5
            elif player2checkeddice[5] == 2:
                play2tiebreaker = play2tiebreaker + 6
            count = 1
            
    ####Four Kind
    elif play1rank == 7 and play2rank == 7:
        while count != 1:
            if player1checkeddice[0] == 4:
                play1tiebreaker = 1
            elif player1checkeddice[1] == 4:
                play1tiebreaker = 2
            elif player1checkeddice[2] == 4:
                play1tiebreaker = 3
            elif player1checkeddice[3] == 4:
                play1tiebreaker = 4
            elif player1checkeddice[4] == 4:
                play1tiebreaker = 5
            elif player1checkeddice[5] == 4:
                play1tiebreaker = 6
            count = 1
        count = 0
        while count != 1:
            if player2checkeddice[0] == 4:
                play2tiebreaker = 1
            elif player2checkeddice[1] == 4:
                play2tiebreaker = 2
            elif player2checkeddice[2] == 4:
                play2tiebreaker = 3
            elif player2checkeddice[3] == 4:
                play2tiebreaker = 4
            elif player2checkeddice[4] == 4:
                play2tiebreaker = 5
            elif player2checkeddice[5] == 4:
                play2tiebreaker = 6
            count = 1
    ####Five Kind
    elif play1rank == 8 and play2rank == 8:
        while count != 1:
            if player1checkeddice[0] == 5:
                play1tiebreaker = 1
            elif player1checkeddice[1] == 5:
                play1tiebreaker = 2
            elif player1checkeddice[2] == 5:
                play1tiebreaker = 3
            elif player1checkeddice[3] == 5:
                play1tiebreaker = 4
            elif player1checkeddice[4] == 5:
                play1tiebreaker = 5
            elif player1checkeddice[5] == 5:
                play1tiebreaker = 6
            count = 1
        count = 0
        while count != 1:
            if player2checkeddice[0] == 5:
                play2tiebreaker = 1
            elif player2checkeddice[1] == 5:
                play2tiebreaker = 2
            elif player2checkeddice[2] == 5:
                play2tiebreaker = 3
            elif player2checkeddice[3] == 5:
                play2tiebreaker = 4
            elif player2checkeddice[4] == 5:
                play2tiebreaker = 5
            elif player2checkeddice[5] == 5:
                play2tiebreaker = 6
            count = 1
            
    if play1tiebreaker > play2tiebreaker:
        winner = "player one"
    elif play2tiebreaker > play1tiebreaker:
        winner = "player two"
    elif play1tiebreaker == play2tiebreaker:
        winner = "tie"    
    win(winner)


def win(winner):
    global playeronescore,playertwoscore
    if winner == "player one":
        WINNERmessagebox = messagebox.showinfo("Dice Poker", "player one wins round")
        playeronescore = playeronescore + 1
        currentp1scorelabel = Label(GAMEGUI, text = str(playeronescore)).place(x = 960, y = 80)
    elif winner == "player two":
        WINNERmessagebox = messagebox.showinfo("Dice Poker", "player two wins round")
        playertwoscore = playertwoscore + 1
        currentp2scorelabel = Label(GAMEGUI, text = str(playertwoscore)).place(x = 960, y = 110)
    elif winner == "tie":
        WINNERmessagebox = messagebox.showinfo("Dice Poker", "This round is a tie")
        playeronescore = playeronescore + 1
        currentp1scorelabel = Label(GAMEGUI, text = str(playeronescore)).place(x = 960, y = 80)
        playertwoscore = playertwoscore + 1
        currentp2scorelabel = Label(GAMEGUI, text = str(playertwoscore)).place(x = 960, y = 110)
    nextround()

def Next1():
    global nextvar
    if nextvar == 5:
        nextvar = 6
        DiceCheck()
#saving scores
def SaveScores(winner):
    try:
        input_file = open('PokerDiceScores.dat', 'rb')#opens file
        scores = pickle.load(input_file)#loads data into variable
        scores#don't know what this is for was there when I read the book for last project
        if winner == "player one wins match":
            scores[0] = scores[0] + 1
            output_file = open('PokerDiceScores.dat', 'wb')
            pickle.dump(scores, output_file)#dumps data
            output_file.close()#closes file
        elif winner == "player two wins match":
            scores[1] = scores[1] + 1
            output_file = open('PokerDiceScores.dat', 'wb')
            pickle.dump(scores, output_file)
            output_file.close()  
        elif winner == "match ends in tie":
            scores[2] = scores[2] + 1
            output_file = open('PokerDiceScores.dat', 'wb')
            pickle.dump(scores, output_file)
            output_file.close()
    except:#incase there isn't a data file
        scores = [0,0,0]
        if winner == "player one wins match":
            scores[0] = scores[0] + 1
            output_file = open('PokerDiceScores.dat', 'wb')#opens file
            pickle.dump(scores, output_file)#dumps data
            output_file.close()#closes file
        elif winner == "player two wins match":
            scores[1] = scores[1] + 1
            output_file = open('PokerDiceScores.dat', 'wb')
            pickle.dump(scores, output_file)
            output_file.close()  
        elif winner == "match ends in tie":
            scores[2] = scores[2] + 1
            output_file = open('PokerDiceScores.dat', 'wb')
            pickle.dump(scores, output_file)
            output_file.close()
####GUI            

MAINGUI = Tk()#stores gui into variable
global GAMEGUI, GAMESTARTED
GAMESTARTED = False

#prevents user from opening multiple games
def STARTGAMECHECK():
    global GAMESTARTED
    if GAMESTARTED == False:
        GAMESTARTED = True
        STARTGAME()
    elif GAMESTARTED == True:
        GAMESTARTEDmessagebox = messagebox.showinfo('Dice Poker',
                                                    'A game is already open')

#GameGUI
def STARTGAME():
    global GAMEGUI, rounds, playeronescore, playertwoscore
    GAMEGUI = Toplevel()#stores secondary window in variable
      
    GAMEGUI.geometry('1200x700')#sets size for window
    GAMEGUI.title("Poker Dice")#sets title
    #Titlelabel = Label(text = "Poker Dice").grid(row = 0, column = 0, sticky = W)#makes label, .grid is for position
    Dicelabel = Label(GAMEGUI,text = "Player one's dice:").place(x = 0, y = 50)
    AIDicelabel = Label(GAMEGUI,text = "Player two's Dice:").place(x = 0, y = 150)

    Roundslabel = Label(GAMEGUI, text = "Round:").place(x = 850, y = 50)
    currentroundlabel = Label(GAMEGUI, text = str(rounds)).place(x = 900, y = 50)
    
    p1scorelabel = Label(GAMEGUI, text = "Player One's Score:").place(x = 850, y = 80)
    currentp1scorelabel = Label(GAMEGUI, text = str(playeronescore)).place(x = 960, y = 80)
    
    p2scorelabel = Label(GAMEGUI, text = "Player Two's Score:").place(x = 850, y = 110)
    currentp2scorelabel = Label(GAMEGUI, text = str(playertwoscore)).place(x = 960, y = 110)

    NewGameButton = Button(GAMEGUI,text = "New Game", command = NewGame).place(x = 0, y = 0)

    QuitButton = Button(GAMEGUI,text = "Quit", command = MAINGUI.destroy).place(x = 1148, y = 0)#makes button
    GenDiceButton = Button(GAMEGUI,text = "Roll Dice", command = Dice).place(x = 200, y = 445)
    CheckMatchWinnerButton = Button(GAMEGUI,text = "Check Winner", command = Next1).place(x = 725, y = 445)
    
    SwapDice1 = Button(GAMEGUI,text = "Swap First Dice", command = SwapButton1).place(x = 216, y = 300)
    SwapDice2 = Button(GAMEGUI,text = "Swap Second Dice", command = SwapButton2).place(x = 336, y = 300)
    SwapDice3 = Button(GAMEGUI,text = "Swap Third Dice", command = SwapButton3).place(x = 475, y = 300)
    SwapDice4 = Button(GAMEGUI,text = "Swap Forth Dice", command = SwapButton4).place(x = 600, y = 300)
    SwapDice5 = Button(GAMEGUI,text = "Swap Fifth Dice", command = SwapButton5).place(x = 726, y = 300)
    finishedswapping = Button(GAMEGUI,text = "Swap Selected Dice", command = swappingcomplete).place(x = 216, y = 350)
        
    
#ScoresGUI
def SCORES():
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

    SCORESGUI.geometry('500x500')
    SCORESGUI.title("Poker Dice")

    p1winsLabel = Label(SCORESGUI, text = "Player One's wins: ").place(x = 100, y = 100)
    p2winsLabel = Label(SCORESGUI, text = "Player Twos's wins: ").place(x = 100, y = 150)
    ptiesLabel = Label(SCORESGUI, text = "Player Ties: ").place(x = 100, y = 200)
    
    p1scoresLabel = Label(SCORESGUI, text = scores[0]).place(x = 225, y = 100)
    p2scoresLabel = Label(SCORESGUI, text = scores[1]).place(x = 225, y = 150)
    ptiesscoresLabel = Label(SCORESGUI, text = scores[2]).place(x = 170, y = 200)
    
    QuitButton = Button(SCORESGUI,text = "Quit", command = MAINGUI.destroy).place(x = 448, y = 0)
    CloseButton = Button(SCORESGUI,text = "Close", command = SCORESGUI.destroy).place(x = 448, y = 400)
    
#Rules GUI
def Rules():
    
    RULESGUI = Toplevel()
    RULESGUI.geometry('700x500')
    RULESGUI.title("Poker Dice")

    RulesLabel = Label(RULESGUI, text = "Rules of Dice Poker:").place(x = 25, y = 50)
    RulesLabel1 = Label(RULESGUI, text = "The aim of dice poker is to get a superior combination compared to your opponent.").place(x = 45, y = 70)
    RulesLabel2 = Label(RULESGUI, text = "There are 6 combinations, from highest to lowest:").place(x = 55, y = 90)
    RulesLabel3 = Label(RULESGUI, text = "Five of a kind: Five dice showing the same value").place(x = 65, y = 110)
    RulesLabel4 = Label(RULESGUI, text = "Four of a kind: Four dice showing the same value").place(x = 65, y = 130)
    RulesLabel5 = Label(RULESGUI, text = "Full House: A pair and a three of a kind").place(x = 65, y = 150)
    RulesLabel6 = Label(RULESGUI, text = "Three of a kind: Three dice showing the same value").place(x = 65, y = 170)
    RulesLabel7 = Label(RULESGUI, text = "Two pairs: dice showing two matched pairs of values").place(x = 65, y = 190)
    RulesLabel8 = Label(RULESGUI, text = "One pair: dice showing a single matched pair of values").place(x = 65, y = 210)

    HowtoPlayLabel =  Label(RULESGUI, text = "How to play Dice Poker:").place(x = 25, y = 300)
    Step1Label = Label(RULESGUI, text = "Step 1: Roll the Dice").place(x = 45, y = 320)
    Step2Label = Label(RULESGUI, text = "Step 2: Swap the dice using the Swap Dice buttons. When finished, click the 'Swap Selected Dice' button").place(x = 45, y = 340)
    Step3Label = Label(RULESGUI, text = "Step 3: Check the winner with the 'Check Winner' button. Repeat these steps until someone wins the match.").place(x = 45, y = 360)

    QuitButton = Button(RULESGUI,text = "Quit", command = MAINGUI.destroy).place(x = 648, y = 0)
    CloseButton = Button(RULESGUI,text = "Close", command = RULESGUI.destroy).place(x = 648, y = 400)

#MainGUI
MAINGUI.geometry('500x500')
MAINGUI.title("Poker Dice")

StartButton = Button(MAINGUI, text = "START GAME", command = STARTGAMECHECK).place(x=100,y=200)
ScoresButton = Button(MAINGUI, text = "SCORES", command = SCORES).place(x = 300, y =200)
QuitButton = Button(MAINGUI,text = "Quit", command = MAINGUI.destroy).place(x = 448, y = 0)
RulesButton = Button(MAINGUI, text = "Rules and How to Play", command = Rules).place(x = 80, y = 300)
MAINGUI.mainloop()#Keeps GUI in a loop so it doesn't close when app is launched

                    
