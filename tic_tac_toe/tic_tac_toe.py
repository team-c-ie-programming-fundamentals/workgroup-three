#%% 1.A

#In this list we simply compare if the condition we need
# happens three times in a row. The elifs and else are just alternatives
#where the "x" team does not win. We access the elements with "double" 
#index notation. 

testlist = [['x','o','x'],['x','x','x'], ['o','o','o']]

def solved_horizontal(lst):

        if lst[0][0] == lst[0][1]== lst[0][2] == 'x':
            return True
        elif lst[1][0] == lst[1][1]==lst[1][2] == 'x':
            return True
        elif lst[2][0] == lst[2][1]==lst[2][2] == 'x':
            return True
        else:
            return False


#1.B

#Optimized version for boards bigger than 3x3
#The upper function wokrs by strictly comparing
#when the board is exactly 3X3. 
            
#We nest two for loops and we evaluate each one. We evaluate horizontaly
 #form left to right, as for loops do, so we don't need to indicate any 
#special jumps between the inner and outer list.            
            
def solved_horizontal_unlimited(board): 
    
    board_lenght = len(board)
    
    
    for line in board: 
        counter = 0 
        
        for element in line:
            if element == "x":
                counter += 1
                if counter == board_lenght:
                    return True  

#%% Linear Search Function we will use later. 
            
def linear(elem, lst):
    for i in range(len(lst)):
        if elem == lst[i]:
            return True
        else:
            return False


#%%

testlist_unl = [['x','o','x','o','x'],
                ['x','x','x','o','x'], 
                ['o','o','o','x','x'], 
                ['x','x','x','o','x'], 
                ['o','o','o','x','x']]            
        

testlist_unl2 = [['x','o','x','o','x'],
                 ['x','x','o','o','x'],
                 ['o','o','x','x','x'], 
                 ['x','x','x','x','x'], 
                 ['x','o','x','x','x']]            

                
board = [['x', 'o', 'x'], 
         ['o', 'x', 'o'], 
         ['x', 'x', 'x']] 


#%% 2.A

testlist_vertical = [['x','o','x'], 
                     ['o','o','x'], 
                     ['x','o','x']]


#Same approach as the horizontal 3x3 version. 

def solved_vertical(lst):
    if lst[0][0]==lst[1][0]==lst[2][0] == 'x':
        return True
    elif lst[0][1]==lst[1][1]==lst[2][1]== 'x':
        return True
    elif lst[0][2]==lst[1][2]==lst[2][2]== 'x':
        return True
    else:
        return False


#2.B
#Optimized/scalable for longer than 3X3. 

#Here, we can't use the same approach as the horizontal unlimited 
#because we need to evaluate vertically, and for loops iterate horizontaly
#from left to right. 
#Insted, we start a while loop conditioned by the lenght of the outer list. 
#We then evaluate and we keep counter for when the 'x' hits. 
#We increase two indexes that basically work as coordinates and we use them
#to tell which element to evaluate next (from up-down and left-right).        
     
def solved_vertical_unlimited(lst):
     
    i = 0
    j = 0

    counter_i = 0
    counter_j = 0
        
    while i < len(lst):

        if lst[i][j] == 'x':
            counter_i +=1
            i +=1
            if counter_i == len(lst):
                return True
        elif lst[i][j] != 'x':
            counter_j += 1
            counter_i += 0
            i = 0
            j += 1
            if counter_j == len(lst):
                return False
    
    
#%%

testlist_diagonal = [['x','o','o'],
                     ['o','x','x'], 
                     ['x','o','x']]


#Same as simple 3x3 of other functions
def solved_diagonal(lst):
    if lst[0][0]==lst[1][1]==lst[2][2]== 'x':
        return True
    if lst[0][2]==lst[1][1]==lst[2][0]== 'x':
        return True
    else:
        return False


#We use the index-as-coordinates approach combinated with a while loop. 
#We will combine two functions: one that evaluates from upper left corner
# to lower right corner of the board; 

def solved_diagonal_left(lst): 
    
    i = 0
    j = 0
    
    counter_i = 0
        
    while i < len(lst):

        if lst[i][j] == 'x':
            counter_i +=1
            i += 1
            j += 1
            if counter_i == len(lst):
                return True
        else:
            return False       
  
#and the second one, viceversa.   
def solved_diagonal_right (lst):
    i = 0
    
    counter_j = 0
    board_len = len(lst) -1 
    while i < len(lst):
          if lst[i][board_len] == 'x':
              counter_j += 1
              i += 1
              board_len = board_len -1
              if counter_j == len(lst):
                  return True     
          else: 
              return False
 
board2 = [['x', 'o', 'x', 'o', 'x'], 
         ['o', 'x', 'x', 'x', 'x'], 
         ['x', 'x', 'x', 'o', 'o'],
         ['x', 'x', 'x', 'o', 'o'],
         ['x', 'x', 'x', 'o', 'x']]
             

#We finally call the "meta" function as a combination of conditions.  
def solved_diagonal_unlimited(lst):
    if solved_diagonal_left(lst) == solved_diagonal_right(lst) == False:
        return False 
    elif solved_diagonal_left(lst) == True:
        return True
    elif solved_diagonal_right(lst) == True:
        return True


#%%

testlist_tictac = [['x','x','x'], 
                   ['o','x','x'], 
                   ['x','x','o']]

#All functions together to tell if x won the game in a 3X3        
def solved_tictactoe(lst):
    if solved_horizontal(lst) == True:
        return str(True) + " by horizontal win"
    elif solved_vertical(lst) == True:
        return str(True) + " by vertical win"
    elif solved_diagonal(lst) == True:
        return str(True) + " by diagonal win"
    else:
        return False
    
    
    
#All functions together to tell if x won the game in an unlimited board 
def solved_tictactoe_unlimited(lst):
    if lst == []: 
        return "empty"
    elif solved_horizontal_unlimited(lst) == True:
        return str(True) + " by horizontal win"
    elif solved_vertical_unlimited(lst) == True:
        return str(True) + " by vertical win"
    elif solved_diagonal_unlimited(lst) == True:
        return str(True) + " by diagonal win"
    else:
        return False
    
        
    

