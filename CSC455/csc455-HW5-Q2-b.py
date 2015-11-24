'''
2b.	Write python code that is going to perform the same computation (find the
 user with the highest “friends_count”)
'''
# import libraries
import re, sqlite3, json
import urllib.request as urllib
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
        # add each value of the friends count in a dictionary with id/name
        dictionary[tDict['id'], tDict['user']['name']] = tDict['user']['friends_count']
        # confirmation print-out of correct dictionary creation
        #print(dictionary)
    except (ValueError, KeyError):
        counter += 1
        #print("tweet {} is corrupted and not included".format(i))

for key, value in dictionary.items():
    if value == max(dictionary.values()):
        print("This is the user  {}, with the highest value of friends at: {}".format(key, value))
print('The # of corrupted tweets in is: ',counter)

