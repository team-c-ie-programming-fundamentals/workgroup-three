# -*- coding: utf-8 -*-

#%%

from rock_paper_scissors import rockpaperscissors 

def test_rockpaperscissors():
    
    assert rockpaperscissors('rock', 'scissors') == "Player 1 won!"
    assert rockpaperscissors('scissors', 'scissors') == "Play again!"
    assert rockpaperscissors('paper','scissors') == "Player 2 won!"

from rock_paper_scissors import rpsls 

def test_rpsls():
    
    assert rpsls('rock', 'scissors') == "Player 1 won!"
    assert rpsls('scissors', 'scissors') == "Play again!"
    assert rpsls('paper','scissors') == "Player 2 won!"
    assert rpsls('spock', 'scissors') == "Player 1 won!"
    assert rpsls('lizzard', 'lizzard') == "Play again!"
    assert rpsls('lizzard','spock') == "Player 1 won!"