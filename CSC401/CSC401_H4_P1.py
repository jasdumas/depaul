''' write a function that excepts a parameter as a
string and compute the average length of all the words in the string'''

def average(string):
    table = str.maketrans(',.?!@#$%^&*', '***********') # replace all punctuation with one value
    string = string.translate(table) # applies the translate based on the table
    string1 = string.replace('*', '') # replaces * with a NULL string and removes all puntuation
    list1 = string1.split() # split string into a list by space
    aveList = [] # initiates a NULL list
 

    for word in list1: # for loop for checking each word in the list
        aveList.append(len(word)) # add the length of each word in the list
        
    return [sum(aveList)/len(aveList)] # add all the list contents and divide by how many there is


print(average('This is the test data to be used for the forth assignment.')) # test sentence
print(average('Does... this? work&&')) # example 1
print(average('a sample sentence')) # example 2
print(average('@@@@I ^LOVE..**# PYTHON,,,')) # example 3
