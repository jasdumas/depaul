# import libraries
import re, sqlite3, json
import urllib.request as urllib
from operator import itemgetter
# open url link/text file
response = urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment5.txt")
# empty list
lines = []
dictionary = {} # if you wanted to re-create the dictionary
counter = 0
# for loop to read through specified amount of lines/tweets
for i in range(7000):  # number should be 7001?
    # read each line/tweet in and specify utf8
    str_response = response.readline().decode("utf8")
    # Read just one line/tweet at a time
    newLine = response.readline()
    # append each line/tweet to the empty list
    lines.append(newLine)
    try:     
        # dictionary object with each file
        tDict = json.loads(str_response)
        # add each value of the tweet text
        dictionary[tDict['id']] = tDict['text']
        # confirmation print-out of correct dictionary creation
        #print(dictionary)
    except (ValueError, KeyError):
        print("exception raised")
        #print("tweet {} is corrupted and not included".format(i))

lst2 = []
dCount = {}
# transform dictionary into a text string for sample code        
for key, value in dictionary.items():
    #word = value.split(' ')
    lst2.append(value)
for sentance in lst2:
#    words = sentance.split(' ')
    #print(words)
    # remove punctuation so that words are counted equally
    table = sentance.maketrans(",.?!@#$%^&*():-_+=<>`~", "$$$$$$$$$$$$$$$$$$$$$$")
    sentance = sentance.translate(table)
    sentance = sentance.replace('$', '')
    words = sentance.split(' ')
        
#text = "This is a frequency count test . The most frequent word will be the word test . Shifting periods to avoid complexity of confusing test and test. in this test sentence"

#words = text.split(' ')

    for word in words: 
        if word not in dCount.keys(): # and word !='':
            dCount[word] = 0
        dCount[word] = dCount[word]+1

    countKeys = dCount.keys()
    countVals = dCount.values()

# We could use dCount.items(), but we want the values to come first and the keys to be second
    countPairs = zip(countVals, countKeys)

    sorted_countPairs = sorted(countPairs, key=itemgetter(0), reverse=True)

# The words are now sorted by descending frequency
    print(sorted_countPairs[:3]) # top 3
