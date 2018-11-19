#%%

def fizzbuzzwhiz(num):
    if num == 0:
        return "undefined"
    elif num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0 and num != 3:
        return "Fizz"
    elif num % 5 == 0 and num != 5:
        return "Buzz"
    elif num >=1:
        for i in range(2, num):
            if (num % i) == 0:
                return num
        else:
                return "Whiz"
                
    else:
                return "Not valid"
       

