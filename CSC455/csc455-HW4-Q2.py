'''
a.	Create a SQL table to contain the following attributes of a tweet:
"created_at", "id_str", "text", "source", "in_reply_to_user_id", 
“in_reply_to_screen_name”, “in_reply_to_status_id”, "retweet_count", “contributors”. 
'''
import sqlite3
import json
import sys

tweetTable = ''' CREATE TABLE tweet
(
    created_at VARCHAR(40),
    id_str VARCHAR(40),
    text VARCHAR(140),
    source VARCHAR(60),
    in_reply_to_user_id VARCHAR(25),
    in_reply_to_screen_name VARCHAR(25),
    in_reply_to_status_id VARCHAR(25),
    retweet_count VARCHAR(25),
    contributors VARCHAR(40)
)
'''

# Open a connection to database
conn = sqlite3.connect("tweetdb.db")

# Request a cursor from the database
cursor = conn.cursor()

# Get rid of the table if we already created it
cursor.execute("DROP TABLE IF EXISTS tweet")

# Create the table in database
cursor.execute(tweetTable)

# Open file for reading
fd = open('/Users/jasminedumas/Desktop/depaul/CSC455/Assignment4.txt', 'r', encoding='utf8')

# Read all lines from the file into allLines variable
allLines = fd.readline().split("EndOfTweet")  # splits data
type(allLines[0]) #check type of first list item, making sure it is a string so that json can load it

# Close the file
fd.close() 

# For each line in the file
for line in allLines:
    try: 
        jsonobject = json.loads(line)
        print(jsonobject['created_at'])
        print(jsonobject['id_str'])
        print(jsonobject['text'])
        print(jsonobject['source'])
        print(jsonobject['in_reply_to_user_id'])
        print(jsonobject['in_reply_to_screen_name'])
        print(jsonobject['in_reply_to_status_id'])
        print(jsonobject['retweeted_status']['retweet_count'],'\n') # dictionary within a dictionary
        print(jsonobject['contributors'])
        break
    except KeyError:
        jsonobject = json.loads(line)
        print(jsonobject['created_at'])  # index 0
        print(jsonobject['id_str'])  # index 2
        print(jsonobject['text']) # index 3
        print(jsonobject['source']) # index 4
        print(jsonobject['in_reply_to_user_id']) # index 8
        print(jsonobject['in_reply_to_screen_name']) # index 10
        print(jsonobject['in_reply_to_status_id']) # index 6
        print(jsonobject['retweet_count']) # regular retweet_count index 16
        print(jsonobject['contributors']) # index 15
#############################
# For each line in the file
for line in allLines:   
    for word2 in line:  # replaces all null with None
        if word2 is 'null':
            word2.replace('null', None)
    valueList = allLines
    
# Load the values into the table (9 column attributes)
cursor.execute("INSERT OR IGNORE INTO tweet VALUES (?,?,?,?,?,?,?,?,?);", 
   (valueList[0], valueList[2], valueList[3], valueList[4], valueList[8], 
    valueList[10], valueList[6], valueList[16], valueList[15]))

# Check what we inserted into the table
allSelectedRows = cursor.execute("SELECT * FROM tweet;").fetchall()

# For every row, print the results of the query above, separated by a tab
for eachRow in allSelectedRows:
    for value in eachRow:
        print (value, "\t",)
    print ("\n",) # \n is the end of line symbol
len(allSelectedRows)

# Finalize inserts and close the connection to the database
conn.commit()
conn.close()   
    
    
    
