def returnThree(x):   # define our function
    return x[0:3]     # What do we want our function to do?
    

ask = input("Please enter a long word: ")   # User prompt

value = returnThree(ask)   # apply function to prompted value

if len(ask) < 3:     # conditions for printing
    print("too tiny")
else:
    print("Here are the first three letters: ", value)        
