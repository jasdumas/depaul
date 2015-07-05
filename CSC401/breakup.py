''' write a function that excepts one paramter, a string then
returns two values, the first value of the number of words
that start with 'a' through 'm' and then the second value
of the number of words 'n' through 'z' '''


def breakup(str1):
    count1 = 0 # define count1
    count2 = 0 # define count2
    str1 = str1.lower()  # case shouldn't matter
    words = str1.split() # creates list of words
    for word in words:  # cycle through list of words
        if word[0] >= 'a' and word[0] <= 'm': ## alphabet is also numeric
            count1  += 1  ## do R-hand side first (= count1 + 1)
        else:
            count2 += 1
    return [count1, count2]  # can only return one thing, make it a list!
    
 



print(breakup('Here is a line of words'))
