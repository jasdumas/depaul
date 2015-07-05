'''
CSC 401: Final Exam (take home)
Problem 1: Counting the lines - 25pts
'''

def line(filename, word):
    infile = open(filename, 'r')  # open file
    content = infile.read()  # reads in as a string
    infile.close()   # close file
    lst = []   # empty list
    new = content.split() # splits the string into lists of lines
    lst2 = []
    
    for lin in new:
        if word in lin:
            lst.append(lin.index(word))  # .index() grabs the first instance in the line w/o duplicates
            #print(lin)
            if lin == word:  # retrieves the exact match of the word
                x = "got it"
                lst2.append(x)
                #print(x)
            
        
    print("The word '{}' occurs in {} lines of file 'innocents.txt'".format(word,len(lst2)))
                 # len() will count all of the empty list contents
    


print(line('innocents.txt', 'spell'))
