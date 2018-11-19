#%%
test_string = "   2,3,4,0     "



def string_calculator(string): 
    
    result = ''.join(string.split()) 
    
    if result == '': 
        return 0
    
    
    else: 
        
        result = result.split(",")
        
        result = [int(number) for number in result]
        
        return (sum(result))
