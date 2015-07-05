'''
CSC 401: Final Exam (take home)
Problem 1: Counting the lines - 25pts
'''

def line(filename, word):
    infile = open(filename, 'r')  # open file
    content = infile.readlines()  # reads in as a string of lines
    infile.close()   # close file
    lst = []   # empty list

    for lin in content:
        if word in lin:
            lst.append(lin.index(word))  # .index() grabs the first instance in the line w/o duplicates

    
    print("The word '{}' occurs in {} lines of file 'innocents.txt'".format(word,len(lst)))
                 # len() will count all of the empty list contents



print(line('innocents.txt', 'hello'))
