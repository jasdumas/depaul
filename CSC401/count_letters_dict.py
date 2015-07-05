'''
Dictionary practice 5/20/15

'''


str1 = "this is a test to see if this works"
#str1 = str1.split()

letters = {}   # empty dictionary letters = {"t":'1', "h": "2"......

strlen = len(str1)   # length of example sentence

for i in range(strlen):
    if str1[i] in letters: # if the first character is in letters dictionary
        letters[str1[i]] += 1
    else:
        letters[str1[i]] = 1 # putting the t, in the key and the 1 in the value space

for letter in letters:
    print("The letter ", letter, " occurs ",
          letters[letter], " times")

''' output:
The letter  o  occurs  2  times
The letter     occurs  8  times
The letter  h  occurs  2  times
The letter  i  occurs  4  times
The letter  a  occurs  1  times
The letter  t  occurs  5  times
The letter  e  occurs  3  times
The letter  w  occurs  1  times
The letter  r  occurs  1  times
The letter  f  occurs  1  times
The letter  s  occurs  6  times
The letter  k  occurs  1  times


output with split string into list from commment str1:
The letter  this  occurs  2  times
The letter  if  occurs  1  times
The letter  works  occurs  1  times
The letter  to  occurs  1  times
The letter  see  occurs  1  times
The letter  test  occurs  1  times
The letter  a  occurs  1  times
The letter  is  occurs  1  times
'''
