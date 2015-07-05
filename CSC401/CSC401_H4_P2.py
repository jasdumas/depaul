''' write a function that accepts a parameter as a file name and
returns the number of occurances of certain words'''

def words(filename):
    infile = open(filename, 'r') # open the file
    content = infile.read() # read the file
    infile.close() # closes file

    one = 'laboratory'
    two = 'Frankenstein'
    three = 'monster'
    
    return [content.count(one), content.count(two), content.count(three)]


print(words('frankenstein.txt'))

