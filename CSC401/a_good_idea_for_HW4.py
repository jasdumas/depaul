''' write a function that accepts a parameter as a file name and
returns the number of occurances of certain words'''

def words(filename):
    countlab = 0 # define start of count for 'laboratory'
    countFrank = 0 # define start of count for 'Frankenstein'
    countmon = 0 # define start of count for 'monster'
    infile = open(filename, 'r') # open the file
    content = infile.read() # read the file
    infile.close() # closes file
#    table = str.maketrans('1234567890,.!@#$%^&*()_-<>?"~`=+:;/|{}[]', '****************************************') # creates table 
#    content = content.translate(table) # applies table with replacement values
#    content = content.replace('*', '') # replaces symbol values with NULL strings
#    contentSplit = content.split() # splits the string into a list

    one = 'laboratory'
    two = 'Frankenstein'
    three = 'monster'
    
##    for word in contentSplit: # a for loop to check individual values in the list
##        if word == 'laboratory':
##            countlab += 1 # adds to the counters
##        elif word == 'Frankenstein':
##            countFrank += 1
##        elif word == 'monster':
##            countmon += 1
    #return [countlab, countFrank, countmon] # you can only return one thing! trick it into a list
    print(content.count(one), content.count(two), content.count(three))


print(words('frankenstein.txt'))

