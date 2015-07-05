''' write a function that excepts two parameters,
a file name and a string, and return the occurance of how many appears'''

def stringCount(filename, str1):
    infile = open(filename, 'r') # 'r' is default & can be left off
    content = infile.read() # read the whole file to the console
    infile.close() # always close your file
    return content.count(str1) # return how many times 'line' appears

print(stringCount('frankenstein.txt', 'laboratory'))  ## output is 4
