# -*- coding: utf-8 -*-

#%%

from tic_tac_toe import solved_tictactoe_unlimited

testlist_unl = [['x','o','x','o','x'],
                ['x','x','x','o','o'], 
                ['o','o','x','x','x'], 
                ['x','x','o','x','x'], 
                ['o','o','o','x','x']]            
        

testlist_unl2 = [['x','o','x','o','x'],
                 ['x','x','o','o','x'],
                 ['o','o','x','x','x'], 
                 ['x','x','x','x','x'], 
                 ['x','o','x','x','x']] 

testlist_unl3 = [['x','o','x','o','x'],
                 ['x','o','o','x','x'],
                 ['o','o','x','x','o'], 
                 ['x','x','o','x','x'], 
                 ['x','o','x','x','x']] 

testlist_4 = []  

def test_solved_all():
    assert solved_tictactoe_unlimited(testlist_unl) == 'True by vertical win'
    assert solved_tictactoe_unlimited(testlist_unl2) == 'True by horizontal win'
    assert solved_tictactoe_unlimited(testlist_unl3) == 'True by vertical win'
    assert solved_tictactoe_unlimited(testlist_4) == "empty"