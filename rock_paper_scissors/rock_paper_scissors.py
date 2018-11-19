#%%

def rockpaperscissors(player1, player2):
    if player1 == "rock":
        if player2 == "paper":
            return "Player 2 won!"
        elif player2 == "rock":
            return "Play again!"
        elif player2 == "scissors":
            return "Player 1 won!"
        
    elif player1 == "scissors":
        if player2 == "scissors":
            return "Play again!"
        elif player2 == "rock":
            return "Player 2 won!"
        elif player2 == "paper":
            return "Player 1 won!"
   
    elif player1 == "paper":
        if player2 == "paper":
            return "Play again!"
        elif player2 == "scissors":
            return "Player 2 won!"
        elif player2 == "rock":
            return "Player 1 won!"# -*- coding: utf-8 -*-

#%%
            
def rpsls(player1, player2):
    if player1 == "rock":
        if player2 == "paper":
            return "Player 2 won!"
        elif player2 == "rock":
            return "Play again!"
        elif player2 == "scissors":
            return "Player 1 won!"
        elif player2 == "spock":
            return "Player 2 won!"
        elif player2 == "lizzard":
            return "Player 1 won!"
        
    elif player1 == "scissors":
        if player2 == "scissors":
            return "Play again!"
        elif player2 == "rock":
            return "Player 2 won!"
        elif player2 == "paper":
            return "Player 1 won!"
        elif player2 == "spock":
            return "Player 2 won!"
        elif player2 == "lizzard":
            return "Player 1 won!"
   
    elif player1 == "paper":
        if player2 == "paper":
            return "Play again!"
        elif player2 == "scissors":
            return "Player 2 won!"
        elif player2 == "rock":
            return "Player 1 won!"
        elif player2 == "spock":
            return "Player 1 won!"
        elif player2 == "lizzard":
            return "Player 2 won!"
    
    elif player1 == "spock":
        if player2 == "paper":
            return "Player 2 won!"
        elif player2 == "scissors":
            return "Player 1 won!"
        elif player2 == "rock":
            return "Player 1 won!"
        elif player2 == "spock":
            return "Play again!"
        elif player2 == "lizzard":
            return "Player 2 won!"
        
    elif player1 == "lizzard":
        if player2 == "paper":
            return "Player 1 won!"
        elif player2 == "rock":
            return "Player 2 won!"
        elif player2 == "scissors":
            return "Player 2 won!"
        elif player2 == "spock":
            return "Player 1 won!"
        elif player2 == "lizzard":
            return "Play again!"