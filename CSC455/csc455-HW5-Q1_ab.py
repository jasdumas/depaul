'''
a.	Create a SQL table for the user entry. It should contain the following 
attributes “id”, “name”, “screen_name”, “description” and “friends_count” and 
modify your SQL table from Assignment 4 to include “user_id” which will be a 
foreign key referencing the user table.

'''
import sqlite3
import json
import sys

tweetuserTable = ''' CREATE TABLE tweetuser
(
    id VARCHAR(40) PRIMARY KEY UNIQUE, 
    name VARCHAR(40), 
    screen_name VARCHAR(40), 
    description VARCHAR(200), 
    friends_count NUMBER, 
    
    CONSTRAINT tu_fk
    FOREIGN KEY (id)
      REFERENCES tweet(user_id)
)
'''

# Open a connection to database
conn = sqlite3.connect("tweetuserdb.db")
# Request a cursor from the database
cursor = conn.cursor()
# Get rid of the table if we already created it
cursor.execute("DROP TABLE IF EXISTS tweetuser")
# Create the table in database
cursor.execute(tweetuserTable)

'''
Original tweet table to be populated from HW4 but modified with user_id
'''
tweetTable = ''' CREATE TABLE tweet
(
    user_id NUMBER PRIMARY KEY UNIQUE,   
    created_at VARCHAR(40),
    id_str VARCHAR(40) ,
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
conn2 = sqlite3.connect("tweetdb.db")
# Request a cursor from the database
cursor2 = conn2.cursor()
# Get rid of the table if we already created it
cursor2.execute("DROP TABLE IF EXISTS tweet")
# Create the table in database
cursor2.execute(tweetTable)

'''
b.	Write python code that is going to read 7000 (only 7000) tweets from the 
Assignment5.txt file from the web and populate both of your tables. It doesn’t
 matter if you load exactly 7000 tweets or “7000 less the bad tweets”, but do 
 not load the entire file.

'''
# import libraries
import re, sqlite3, json
import urllib.request as urllib
# open url link/text file
response = urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt")
# empty list
lines = []
lines2 = [] 
counter = 0
counter2 = 0
# for loop to read through specified amount of lines/tweets
for i in range(100):  # number should be 7001
    # read each line/tweet in and specify utf8
    str_response = response.readline().decode("utf8")
    # Read just one line/tweet at a time
    newLine = response.readline()
    # append each line/tweet to the empty list
    lines.append(newLine)
    ## Original tweet table from HW4
    newLine2 = response.readline()
    lines2.append(newLine2)
    try:
        # create a dictionary to hold all of the lines/tweets by unique id       
        tDict = json.loads(str_response)
        # confirmation print by 'id' key of line/tweets
#        print('For tweet #',i,' the id is: ',tDict['id'], ', username is: ',tDict['user']['name'], 
#              'the screen_name is: ', tDict['user']['screen_name'], ', the description is: ', tDict['user']['description'], 
#              ', the # of friends is: ', tDict['user']['friends_count'], '\n')
#        # Load the values into the table (5 column attributes)
        cursor.execute("INSERT OR IGNORE INTO tweetuser VALUES (?,?,?,?,?);", 
                       (tDict['id'], tDict['user']['name'], tDict['user']['screen_name'], 
                        tDict['user']['description'], tDict['user']['friends_count']))
        ## Original tweet table from HW4
        cursor2.execute("INSERT OR IGNORE INTO tweet VALUES (?,?,?,?,?,?,?,?,?,?);", 
                       (tDict['id'],
                        tDict['user']['created_at'],
                        tDict['user']['id_str'], 
                        tDict['text'], 
                        tDict['source'],
                        tDict['in_reply_to_user_id'], 
                        tDict['in_reply_to_screen_name'], 
                        tDict['in_reply_to_status_id'], 
                        tDict['retweeted_status']['retweet_count'], 
                        tDict['contributors']))                
        # Check what we inserted into the table
        allSelectedRows = cursor.execute("SELECT * FROM tweetuser;").fetchall()
        allSelectedRows2 = cursor2.execute("SELECT * FROM tweet;").fetchall()
        # For every row, print the results of the query above, separated by a tab
        for eachRow in allSelectedRows:
            for value in eachRow:
#                print ('This is in SQL: ',value, "\n",)
                len(allSelectedRows)
        for eachRow in allSelectedRows2:
            for value in eachRow:
#                print ('This is in SQL: ',value, "\n",)
                len(allSelectedRows2)
    except (ValueError, KeyError): # catch both errors
        ## Original HW4 table exception
        cursor2.execute("INSERT OR IGNORE INTO tweet VALUES (?,?,?,?,?,?,?,?,?, ?);", 
                       (tDict['id'],
                        tDict['user']['created_at'],
                        tDict['user']['id_str'], 
                        tDict['text'], 
                        tDict['source'],
                        tDict['in_reply_to_user_id'], 
                        tDict['in_reply_to_screen_name'], 
                        tDict['in_reply_to_status_id'], 
                        tDict['retweet_count'], 
                        tDict['contributors']))              
        counter += 1
        # traditional error print output        
        #print('For tweet #',i,' Tweet is corrupted and it threw a ValueError ',ValueError)
        # create/open a .txt file to append broken tweet/lines to        
        with open("tweeterror.txt", "a") as out_file:
            out_file.write('For tweet {}, Tweet is corrupted and it threw a ValueError \n'.format(i))
        with open("tweeterror.txt", "rt") as in_file:
            # open the error file back up and read contents            
            text = in_file.read()    
            # confirmation print of what was appended to the error file            
            #print(text)
print('The # of corrupted tweets in is: ',counter)
out_file.close()
# Finalize inserts and close the connection to the database
conn.commit()
conn.close() 
conn2.commit()
conn2.close()     

# Homework Question 2 trials
#s = cursor.execute("SELECT id, name FROM tweetuser WHERE friends_count = (SELECT MAX(friends_count) FROM tweetuser);").fetchall()