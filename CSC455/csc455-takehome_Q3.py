'''
3a.	Export the contents of the User table from a SQLite table into a sequence 
of INSERT statements within a file. This is very similar to what you did in 
Assignment 4. However, you have to add a unique ID column which has to be a 
string (you cannot use any numbers). Hint: one possibility is to replace digits
 with letters, e.g., chr(ord('a')+1) gives you a 'b' and chr(ord('a')+2) 
 returns a 'c'
'''

cursor.execute('SELECT COUNT(*) FROM tweetuser;').fetchall()





'''
3b.	Create a similar collection of INSERT for the User table by 
reading/parsing data from the local tweet file that you have saved earlier. 
'''
import json
import codecs
def generateInsertFinal(tablename):
    select = 'SELECT * FROM {};'.format(tablename)
    print(select)
    #lst = []
    #lst2 = []
    fd = open('/Users/jasminedumas/Desktop/depaul/CSC455/tweetfinal.txt', 'r',  encoding='utf8')
    # Read all lines from the file into allLines variable
    allLines = fd.readlines()
    # Close the file
    fd.close() 

    # For each line in the file
    for line in allLines:
        jsonobject = json.loads(line)
    
    
        tweet_u = (jsonobject['id_str'],jsonobject['user']['name'], jsonobject['user']['screen_name'], jsonobject['user']['description'], jsonobject['user']['friends_count'])
    #print("INSERT OR IGNORE INTO tweetuser VALUES {};".format( tweet_u))

        with open("generateInsertFinal.txt", "a",  encoding="utf-8") as out_file:
            out_file.write("INSERT OR IGNORE INTO tweetuser VALUES {};".format( tweet_u))
        with open("generateInsertFinal.txt", "rt", encoding="utf-8") as in_file:
            text = in_file.read()    
    print(text)
    out_file.close()
                    
tablename = "tweetuser"
generateInsertFinal(tablename)