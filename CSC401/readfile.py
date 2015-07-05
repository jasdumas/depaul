''' don't need address directory if both the .py program and the text file
are in the same directory'''

def numChars(filename):
    infile = open(filename, 'r') # 'r' is default & can be left off
    content = infile.read() # read the whole file to the console
    infile.close() # always close your file
    return len(content)

print(numChars('example.txt'))
