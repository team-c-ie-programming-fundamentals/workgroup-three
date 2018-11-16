# -*- coding: utf-8 -*-

#%%
from rock_paper_scissors import rockpaperscissors 

def test_rockpaperscissors():
    
    assert rockpaperscissors('rock', 'scissors') == "Player 1 won!"
    assert rockpaperscissors('scissors', 'scissors') == "Play again!"
    assert rockpaperscissors('paper','scissors') == "Player 2 won!"
    