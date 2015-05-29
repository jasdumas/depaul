'''
While - indefinite loop
'''


total = 0 # set your totals outside of the while loops
moredata = input("do you have any data? (y to continue) ") # original prompt, sets the condition


while moredata in ['y', 'Y', 'yes', 'Yes', 'OK']: # check to see answer in while condition (T or F)
    score = eval(input('Enter the score: ')) # a tally of the score
    total += score  # adds to the counter
    moredata = input('do you have any more data? ') # repeat prompt, if yes then the loop continues, re-set condition

print('The total is: ', total)
