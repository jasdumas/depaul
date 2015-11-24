'''
Take-home final
a.	Create a 3rd table incorporating the Geo table (in addition to tweet and 
user tables that you already have) and extend your schema accordingly.
You will need to generate an ID for the Geo table primary key (you may use any 
value or combination of values as long as it is unique) for that table and link
 it to the Tweet table (foreign key should be in the Tweet table because there 
 can be multiple tweets sent from the same location). In addition to the 
 primary key column, the geo table should have “type”, 
 “longitude” and “latitude” columns.
'''
import sqlite3
import json
import sys

'''
Tweet table from HW 4
'''
tweetTable = ''' CREATE TABLE tweet
(
    user_id NUMBER ,   
    created_at VARCHAR(40),
    id_str VARCHAR(40) PRIMARY KEY UNIQUE,
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
Tweet user table from HW 5
'''
tweetuserTable = ''' CREATE TABLE tweetuser
(
    id VARCHAR(40) PRIMARY KEY UNIQUE, 
    name VARCHAR(40), 
    screen_name VARCHAR(40), 
    description VARCHAR(200), 
    friends_count NUMBER, 
    
    CONSTRAINT tu_fk
    FOREIGN KEY (id)
      REFERENCES tweet(id_str)
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
Tweet GEO table for take-home final
'''
tweetGeoTable = ''' CREATE TABLE tweetgeo
(
    gID VARCHAR(40) PRIMARY KEY UNIQUE, 
    type VARCHAR(100), 
    latitude VARCHAR(100),    
    longitude VARCHAR(100),  
    
    CONSTRAINT tg_fk
    FOREIGN KEY (gID)
      REFERENCES tweet(id_str)

)
'''
# Open a connection to database
conn3 = sqlite3.connect("tweetgeodb.db")
# Request a cursor from the database
cursor3 = conn3.cursor()
# Get rid of the table if we already created it
cursor3.execute("DROP TABLE IF EXISTS tweetgeo")
# Create the table in database
cursor3.execute(tweetGeoTable)
##############################################################################
'''
b.  Use python to download from the web and save to a local text file (not into
 database yet) at least 500,000 lines worth of tweets. Test your code with 
 fewer rows first – you can reduce the number of tweets if your computer is 
 running too slow to handle 500K tweets in a reasonable time. How long did it 
 take to save?
NOTE: Do NOT call read() or readlines() without any parameters. 
That command will attempt to read the entire file and you only need 500K rows.
'''
# import libraries
import sqlite3
import sys
import re, sqlite3, json
import urllib.request as urllib
import codecs
# open url link/text file
response = urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt")
counter = 0
# can calculate program runtime / performance
import time
start = time.time() # beginning of loop
# for loop to write tweets to a file 
for i in range(1000):  # number should be 500000
     # read each line/tweet in and specify utf8
    str_response = response.readline().decode("utf8")   
    #try:
       # first save the tweets to a local text file
    with open("tweetfinal.txt", "a", encoding="utf-8") as out_txt_file:
        out_txt_file.write(str_response)
    with open("tweetfinal.txt", "r", encoding="utf-8") as in_txt_file:
        # open the error file back up and read contents            
        text = in_txt_file.read()    
    #except (TypeError):
    counter += 1
print("Part 1-B parameters: \n")
print("tweets loaded to file: ", counter)
end = time.time() # end of loop
print ("Difference is ", round((end-start),3), 'seconds')
print ("Performance : ", round(100000/(end-start), 3), ' operations per second \n')
print("-"*30)
##############################################################################
'''
c.	Repeat what you did in part-b, but instead of saving tweets to the file,
 populate the 3-table schema that you created in SQLite. Be sure to execute 
 commit and verify that the data has been successfully loaded (report row 
 counts for each of the 3 tables).
If you use the posted example code be sure to turn off batching for this part.
 (i.e., batchRows set to 1). How long did this step take?
'''
# previous library are already imported
# empty list
lines = []
lines2 = [] 
counter2 = 0
# can calculate program runtime / performance
import time
start2 = time.time() # beginning of loop
# for loop to read through specified amount of lines/tweets
for i in range(1000):  # number should be 500000
    str_response = response.readline().decode("utf-8")
    newLine = response.readline()
    lines.append(newLine)
    newLine2 = response.readline()
    lines2.append(newLine2)
    try:
        # create a dictionary to hold all of the lines/tweets by unique id       
        tDict = json.loads(str_response)
        
        cursor2.execute("INSERT OR IGNORE INTO tweet VALUES (?,?,?,?,?,?,?,?,?,?);", 
                       (tDict['user']['id_str'],
                        tDict['user']['created_at'],                        
                        tDict['id_str'],  # PK 
                        tDict['text'], 
                        tDict['source'],
                        tDict['in_reply_to_user_id'], 
                        tDict['in_reply_to_screen_name'], 
                        tDict['in_reply_to_status_id'], 
                        tDict['retweeted_status']['retweet_count'], 
                        tDict['contributors']))               
        ## Original tweetuser table from HW5
        cursor.execute("INSERT OR IGNORE INTO tweetuser VALUES (?,?,?,?,?);", 
                       (tDict['id_str'],   #FK #PK
                        tDict['user']['name'], 
                        tDict['user']['screen_name'], 
                        tDict['user']['description'], 
                        tDict['user']['friends_count']))
        ## tweetgeo table for take-home final
        cursor3.execute("INSERT OR IGNORE INTO tweetgeo VALUES (?,?,?,?);", 
                        (tDict['id_str'], #FK
                        tDict['geo']['type'], 
                        tDict['geo']['coordinates'][0], 
                        tDict['geo']['coordinates'][1]))  
        # Check what we inserted into the table
        allSelectedRows2 = cursor2.execute("SELECT * FROM tweet;").fetchall()        
        allSelectedRows = cursor.execute("SELECT * FROM tweetuser;").fetchall()
        allSelectedRows3 = cursor3.execute("SELECT * FROM tweetgeo;").fetchall()
        # For every row, print the results of the query above, separated by a tab
        for eachRow in allSelectedRows:
            for value in eachRow:
#                print ('This is in SQL: ',value, "\n",)
                len(allSelectedRows)
        for eachRow in allSelectedRows2:
            for value in eachRow:
#                print ('This is in SQL: ',value, "\n",)
                len(allSelectedRows2)
        for eachRow in allSelectedRows3:
            for value in eachRow:
#                print ('This is in SQL: ',value, "\n",)
                len(allSelectedRows3)
    except (ValueError, KeyError, UnicodeEncodeError, TypeError): # catch multiple errors
        ## Original HW4 table exception b/c of retweet count placement
        cursor2.execute("INSERT OR IGNORE INTO tweet VALUES (?,?,?,?,?,?,?,?,?,?);", 
                       (tDict['user']['id_str'],
                        tDict['user']['created_at'],                        
                        tDict['id_str'], #PK
                        tDict['text'], 
                        tDict['source'],
                        tDict['in_reply_to_user_id'], 
                        tDict['in_reply_to_screen_name'], 
                        tDict['in_reply_to_status_id'], 
                        tDict['retweet_count'], 
                        tDict['contributors']))              
        counter2 += 1
print("Part 1-C parameters: \n")
print('tweets populated in sql table: ',counter2)
#print('tweet row count {}, tweetuser row count {}, tweetgeo row count {}.'.format(len(allSelectedRows2), len(allSelectedRows), len(allSelectedRows3)))
end2 = time.time() # end of loop
print ("Difference is ", round((end2-start2), 3), 'seconds')
print ("Performance : ", round(100000/(end2-start2), 3), ' operations per second \n')
print("-"*30)

##############################################################################
'''
d.	Use your locally saved tweet file (created in part-b) to repeat the 
database population step from part-c. That is, load 500,000 tweets into the 
3-table database using your saved file with tweets (do not use the URL to read 
twitter data). How does the runtime compare with part-c?
'''
#Open file for reading that was created in part-b
fd = open('/Users/jasminedumas/Desktop/depaul/CSC455/tweetfinal.txt', 'r', encoding='utf8')
# Read all lines from the file into allLines variable
allLines = fd.readlines()#.split()  # splits data - not sure what to split on, but needs to read each line
# Close the file
fd.close() 
import time
start3 = time.time() # beginning of loop
# For each line in the file
for line in allLines:
    jsonobject = json.loads(line)
    
    if 'retweeted_status' in jsonobject.keys():
        retweetcount = jsonobject['retweeted_status']['retweet_count']
    else:
        retweetcount = jsonobject['retweet_count']
    # SQL inserts to tweet table
    tweetvalues = (jsonobject['user']['id_str'], jsonobject['created_at'],jsonobject['id_str'], jsonobject['text'], jsonobject['source'],jsonobject['in_reply_to_user_id'], jsonobject['in_reply_to_screen_name'], jsonobject['in_reply_to_status_id'], retweetcount, jsonobject['contributors']) 
    cursor2.execute("INSERT OR REPLACE INTO tweet VALUES(?,?,?,?,?,?,?,?,?,?);",tweetvalues)
    # SQL inserts to tweetuser table
    tweet_u = (jsonobject['id_str'],jsonobject['user']['name'], jsonobject['user']['screen_name'], jsonobject['user']['description'], jsonobject['user']['friends_count'])
    cursor.execute("INSERT OR IGNORE INTO tweetuser VALUES (?,?,?,?,?);", tweet_u)
    # SQL inserts to tweetgeo table

    if jsonobject['geo'] != None:
        geotype = jsonobject['geo']['type']
        lat = jsonobject['geo']['coordinates'][0]
        long =jsonobject['geo']['coordinates'][1]
        tweet_geo = (jsonobject['id_str'], geotype, lat, long)
        cursor3.execute("INSERT OR IGNORE INTO tweetgeo VALUES (?,?,?,?);", tweet_geo)
    else:
        pass
        #tweet_geo = (jsonobject['id_str'], None, None, None)
        #cursor3.execute("INSERT OR IGNORE INTO tweetgeo VALUES (?,?,?,?);", tweet_geo)
        
#    tweet_geo = (jsonobject['id_str'], jsonobject['geo']['type'], jsonobject['geo']['coordinates'][0], jsonobject['geo']['coordinates'][1])
#    cursor3.execute("INSERT OR IGNORE INTO tweetgeo VALUES (?,?,?,?);", tweet_geo)
    
#for row in cursor2.execute("SELECT * FROM tweet;"):
#    for column in row:
#        print(column)
#    print("\n",)
#for row in cursor3.execute("SELECT * FROM tweetgeo;"):
#    for column in row:
#        print(column)
#    print("\n",)
#for row in cursor.execute("SELECT * FROM tweetuser;"):
#    for column in row:
#        print(column)
#    print("\n",)

end3 = time.time() # end of loop
print("Part 1-D parameters: \n")
print ("Difference is ", round((end3-start3), 3), 'seconds')
print ("Performance : ", round(100000/(end3-start3), 3), ' operations per second \n')
print("-"*30)

##############################################################################
'''
e.	Re-run the previous step with batching size of 500 (i.e. by inserting 500 
rows at a time with executemany). You can adapt the posted example code. How 
does the runtime compare when batching is used?
'''
start4 = time.time()
def loadTweets(tweetLines):

    # Collect multiple rows so that we can use "executemany".  We do
    # not want to collect all of the numLines rows because there may
    # not be enough memory for that. So we insert batchRows at a time
    batchRows = 500
    batchedInserts = []
    batchedInserts2 = []
    batchedInserts3 = []

    # as long as there is at least one line remaining
    while len(tweetLines) > 0:
        line = tweetLines.pop(0) # take off the first element from the list, removing it
    
        jsonobject = json.loads(line)
        
        # tweet table
        newRow = [] # hold individual values of to-be-inserted row
        tweetKeys = ['id_str','created_at','text','source','in_reply_to_user_id', 
        'in_reply_to_screen_name', 'in_reply_to_status_id', 'retweet_count', 'contributors']
        
        for key in tweetKeys:
            # Treat '', [] and 'null' as NULL
            if jsonobject[key] in ['',[],'null']:
                newRow.append(None)
            else:
                newRow.append(jsonobject[key])
        
        # tweetuser table
        newRow2 = [] # hold individual values of to-be-inserted row
        tweetKeys2 = ['id_str',['user']['name'], ['user']['screen_name'], ['user']['description'], ['user']['friends_count']]
    
        for key in tweetKeys2:
            # Treat '', [] and 'null' as NULL
            if jsonobject[key] in ['',[],'null']:
                newRow2.append(None)
            else:
                newRow2.append(jsonobject[key])

        # tweetgeo table
        newRow3 = [] # hold individual values of to-be-inserted row
        tweetKeys3 = ['id_str', ['geo']['type'], ['geo']['coordinates'][0], jsonobject['geo']['coordinates'][1]]
     
        for key in tweetKeys3:
            # Treat '', [] and 'null' as NULL
            if jsonobject[key] in ['',[],'null']:
                newRow3.append(None)
            else:
                newRow3.append(jsonobject[key])

        # Add the new row to the collected batch
        batchedInserts.append(newRow)
        batchedInserts2.append(newRow2)
        batchedInserts3.append(newRow3)

        # If we have reached # of batchRows, use executemany to insert what we collected
        # so far, and reset the batchedInserts list back to empty
        if len(batchedInserts) >= batchRows or len(tweetLines) == 0:
            cursor2.executemany('INSERT INTO tweet VALUES(?,?,?,?,?,?,?,?,?);', batchedInserts)
            # Reset the batching process
            batchedInserts = []
        if len(batchedInserts2) >= batchRows or len(tweetLines) == 0:
            cursor.executemany('INSERT INTO tweetuser VALUES(?,?,?,?,?);', batchedInserts2)
            # Reset the batching process
            batchedInserts2 = []
        if len(batchedInserts3) >= batchRows or len(tweetLines) == 0:
            cursor3.executemany('INSERT INTO tweetgeo VALUES(?,?,?,?);', batchedInserts3)
            # Reset the batching process
            batchedInserts3 = []

#start4 = time.time()

fd = open('/Users/jasminedumas/Desktop/depaul/CSC455/tweetfinal.txt', 'r', encoding='utf8')
allLines = fd.readlines()

end4   = time.time()
print("Part 1-E parameters: \n")
print ("loadTweets took ", round((end4-start4), 3), ' seconds.')
print ("tweet-Loaded ", cursor2.execute('SELECT COUNT(*) FROM tweet;').fetchall()[0], " rows")
print ("tweetuser-Loaded ", cursor.execute('SELECT COUNT(*) FROM tweetuser;').fetchall()[0], " rows")
print ("tweetgeo-Loaded ", cursor3.execute('SELECT COUNT(*) FROM tweetgeo;').fetchall()[0], " rows")
print("-"*30)
##############################################################################
'''
2a.	Write and execute SQL queries to do the following. Don’t forget to report 
the running times in each part – you do not need to report the output:
'''
print("Part 2a runtime parameters: \n")
# i 
start5 = time.time()
cursor2.execute("SELECT * FROM tweet WHERE id_str LIKE '%44%' OR id_str LIKE '%77%';").fetchall()
end5   = time.time()
print ("i-Difference is ", round((end5-start5), 3), 'seconds')
print ("Performance : ", round(100000/(end5-start5), 3), ' operations per second ')

# ii
start6 = time.time()
cursor2.execute("SELECT COUNT( DISTINCT in_reply_to_user_id) FROM tweet ;").fetchall()
end6   = time.time()
print ("ii-Difference is ", round((end6-start6), 3), 'seconds')
print ("Performance : ", round(100000/(end6-start6), 3), ' operations per second ')

# iii - I could also set it equal to 140 since that is the max chars for a tweet
start7= time.time()
cursor2.execute("SELECT * FROM tweet WHERE length(text) = (SELECT MAX(length(text)) FROM tweet);").fetchall() 
end7   = time.time()
print ("iii-Difference is ", round((end7-start7), 3), 'seconds')
print ("Performance : ", round(100000/(end7-start7), 3), ' operations per second ')

# iv
start8= time.time()
cursor3.execute("SELECT AVG(longitude), AVG(latitude) FROM tweetgeo GROUP BY gID;").fetchall()
end8   = time.time()
print ("iv-Difference is ", round((end8-start8), 3), 'seconds')
print ("Performance : ", round(100000/(end8-start8), 3), ' operations per second ')

# v
start9 = time.time()
for i in range(10):
    cursor3.execute("SELECT AVG(longitude), AVG(latitude) FROM tweetgeo GROUP BY gID;").fetchall()
end9   = time.time()
print ("v-Difference is ", round((end9-start9), 3), 'seconds')
print ("Performance : ", round(100000/(end9-start9), 3), ' operations per second ')

start10 = time.time()
for i in range(100):
    cursor3.execute("SELECT AVG(longitude), AVG(latitude) FROM tweetgeo GROUP BY gID;").fetchall()
end10   = time.time()
print ("v-Difference is ", round((end10-start10), 3), 'seconds')
print ("Performance : ", round(100000/(end10-start10), 3), ' operations per second ')
print("**SQL query run 1x: {}, 10x: {}, 100x: {}.".format((end8-start8),(end9-start9), (end10-start10)))

n1xscale = round((end8-start8), 3)
n10xscale_exp = round((10*(end8-start8)), 3)
n100xscale_exp = round((100*(end8-start8)), 3)
n10xscale_real = round((end9-start9), 3)
n100xscale_real = round((end10-start10), 3)

# Does the runtime scale linearly? (i.e., does it take 10X and 100X as much time?)
if n10xscale_exp == n10xscale_real:
    print("The 10x run scaled linearly")
else:
    print("The 10x run did not scale linearly")
    
if n100xscale_exp == n100xscale_real:
    print("The 100x run scaled linearly")
else:
    print("The 100x run did not scale linearly")    



############################################################################### 
'''
2b.	Write python code that is going to read the locally saved tweet data file
 from 1-b and perform the equivalent computation for parts 2-i and 2-ii only. 
 How does the runtime compare to the SQL queries?
'''

# i.	Find tweets where tweet id_str contains “44” or “77” anywhere in the column
import json
filename = '/Users/jasminedumas/Desktop/depaul/CSC455/tweetfinal.txt'
infile = open(filename, 'r', encoding='utf8')
content = infile.readlines()
lst = []
start_44 = time.time()
for line in content:
    newline = json.loads(line)
    if 'id_str' in newline:
        lst.append(newline.get('id_str'))
    else: 
        pass
print("Part 2b-1: \n")
for i in lst:
    if "44" in i or "77" in i:
        print(i)
end_44 = time.time()
print("Part 2b-1: \n")
print ("Difference is ", round((end_44-start_44 ), 3), 'seconds')
print ("Performance : ", round(100000/(end_44-start_44), 3), ' operations per second ')
print("-"*30)

# ii.	Find how many unique values are there in the “in_reply_to_user_id” column
lst_unq = []
start_ui = time.time()
for line in content:
    newline = json.loads(line)
    if 'in_reply_to_user_id' in newline:
        lst_unq.append(newline.get('in_reply_to_user_id'))
    else: 
        pass
end_ui = time.time()
print("Part 2b-2: \n")
print("There are:", len(set(lst_unq)), "unique in_reply_to_user_id in the tweet file")
print ("Difference is ", round((end_ui -start_ui), 3), 'seconds')
print ("Performance : ", round(100000/(end_ui -start_ui), 3), ' operations per second ')
print("-"*30)

# EXTRA CREDIT --- iii. Find the tweet(s) with the longest text message
lst_text = []
start_ec = time.time()
for line in content:
    newline = json.loads(line)
    if 'text' in newline:
        lst_text.append(newline.get('text'))
    else: 
        pass
for i in lst_text:
    if len(i) == 140: # twitter text character max is 140!
        print("This is one of the longest tweets at 140 characters:", i)
end_ec = time.time()
print("Part 2b-extra credit: \n")
print ("Difference is ", round((end_ec -start_ec), 3), 'seconds')
print ("Performance : ", round(100000/(end_ec -start_ec), 3), ' operations per second ')
print("-"*30)

##############################################################################
'''
3a.	Export the contents of the User table from a SQLite table into a sequence 
of INSERT statements within a file. This is very similar to what you did in 
Assignment 4. However, you have to add a unique ID column which has to be a 
string (you cannot use any numbers). Hint: one possibility is to replace digits
 with letters, e.g., chr(ord('a')+1) gives you a 'b' and chr(ord('a')+2) 
 returns a 'c'
'''
import random
import string
start_3a = time.time()
export = cursor.execute('SELECT * FROM tweetuser;').fetchall()
for entry in export:
    
    tweet_user_content = ("".join( [random.choice(entry[0]) for i in range(len(entry[0]))]) , entry[0], entry [1], entry[2], entry[3], entry[4])
    print(tweet_user_content)
    with open("generateInsertFinalA.txt", "a",  encoding="utf-8") as out_file:
            out_file.write("INSERT OR IGNORE INTO tweetuser VALUES {};".format(tweet_user_content))
    with open("generateInsertFinalA.txt", "rt", encoding="utf-8") as in_file:
            text = in_file.read() 
end_3a = time.time()
print ("Difference is ", round((end_3a -start_3a), 3), 'seconds')
print ("Performance : ", round(100000/(end_3a -start_3a), 3), ' operations per second ')
print("-"*30)

#print(text)
out_file.close()

##############################################################################
'''
3b.	Create a similar collection of INSERT for the User table by 
reading/parsing data from the local tweet file that you have saved earlier. 
'''
start_3b = time.time()
file = open('/Users/jasminedumas/Desktop/depaul/CSC455/tweetfinal.txt', 'r',  encoding='utf8')
# Read all lines from the file into allLines variable
allLines = file.readlines()
# Close the file
file.close() 
# For each line in the file
for line in allLines:
    jsonobject = json.loads(line)
    tweet_u = ("".join( [random.choice(jsonobject['id_str']) for i in range(len(jsonobject['id_str']))]),jsonobject['id_str'],jsonobject['user']['name'], jsonobject['user']['screen_name'], jsonobject['user']['description'], jsonobject['user']['friends_count'])
    with open("generateInsertFinalB.txt", "a",  encoding="utf-8") as out_fileB:
        out_fileB.write("INSERT OR IGNORE INTO tweetuser VALUES {};".format( tweet_u))
    with open("generateInsertFinalB.txt", "rt", encoding="utf-8") as in_fileB:
        textB = in_fileB.read()    
#print(textB)
end_3b = time.time()
print ("Difference is ", round((end_3b -start_3b), 3), 'seconds')
print ("Performance : ", round(100000/(end_3b -start_3b), 3), ' operations per second ')
print("-"*30)

out_fileB.close()
##############################################################################
'''
4. 1.	Export all three tables (Tweet, User and Geo tables) from the database 
into a |-separated text file. In this part, you do not have to modify the table
 within the database, just output file data (do not generate INSERT statements,
 just raw data)
'''
export1 = cursor.execute('SELECT * FROM tweetuser;').fetchall()
export2 = cursor2.execute('SELECT * FROM tweet;').fetchall()
export3 = cursor3.execute('SELECT * FROM tweetgeo;').fetchall()

##############################################################################
'''
c.	For the User table file add a column (true/false) that specifies whether 
“screen_name” or “description” attribute contains within it the “name” 
attribute of the same user. That is, your output file should contain all of the
 columns from the User table, plus the new column. You do not have to modify 
 the original User table.
'''
for entry in export1:
    for i in entry:
        if i in entry: # [2:3] is the screen_name & description
            a = "True"           
        else:
            a = "False"            
        with open("generateInsertFinal4A.txt", "a",  encoding="utf-8") as out_file4A:
#            new = str(i) + a
            out_file4A.write("{} | {} |\n".format(i, a))
        with open("generateInsertFinal4A.txt", "rt", encoding="utf-8") as in_file4A:
            text4A = in_file4A.read()
print(text4A)

##############################################################################
'''
b.	For the Tweet table, replace NULLs by a reference to ‘Unknown’ entry 
(i.e., the foreign key column that references Geo table should refer to the 
“Unknown” entry you created in part-a. Report how many known/unknown locations 
there were in total (e.g., 10,000 known, 490,000 unknown,  2% locations are available)
'''
count_known = 0
count_unknown = 0
for entry in export2:
    for i in entry:
        if i == None:
            i = 'Unknown'
            count_unknown += 1
        else:
            pass
            count_known += 1
        with open("generateInsertFinal4A.txt", "a",  encoding="utf-8") as out_file4At:
            out_file4At.write("{} |".format(i))
        with open("generateInsertFinal4A.txt", "rt", encoding="utf-8") as in_file4At:
            text4At = in_file4At.read()
print(text4At)
percent = (count_known/count_unknown)*100
print("\n {} known, {} unknown, {}% locations are avaialble.".format(count_known, count_unknown,percent ))
##############################################################################
'''
a.	For the Geo table, create a single default entry for the ‘Unknown’ 
location and round longitude and latitude to a maximum of 4 digits after the decimal.
'''

for entry in export3:
    for i in entry:
        try:
            i = round(float(i), 4)
            print(i)
        except ValueError:
            pass
        if i == None:
            i = 'Unknown'
        else:
            pass
        with open("generateInsertFinal4A.txt", "a",  encoding="utf-8") as out_file_geo:
            out_file_geo.write("{} |".format(i))
        with open("generateInsertFinal4A.txt", "rt", encoding="utf-8") as in_file_geo:
            text_geo = in_file_geo.read()
print(text_geo)

out_file_geo.close()
out_file4A.close()
out_file4At.close()







##############################
##### Finalize and close #####
###############################
conn.commit()
conn.close() 
conn2.commit()
conn2.close()     
conn3.commit()
conn3.close()  