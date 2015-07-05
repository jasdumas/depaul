''' write a function that excepts a parameter,
a file name and splits and returns a count of the total words'''

def splitit(filename):
    infile = open(filename, 'r') # 'r' is default & can be left off
    content = infile.read() # read the whole file to the console
    infile.close() # always close your file
    wordList = content.split()
    print(wordList)
    return len(wordList) # return how many times 'line' appears

print(splitit('example.txt'))  ## output is 4
