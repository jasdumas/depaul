############################################################################## 
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

# ii.	Find how many unique values are there in the “in_reply_to_user_id” column
lst_unq = []
for line in content:
    newline = json.loads(line)
    if 'in_reply_to_user_id' in newline:
        lst_unq.append(newline.get('in_reply_to_user_id'))
    else: 
        pass
print("Part 2b-2: \n")
print("There are:", len(set(lst_unq)), "unique in_reply_to_user_id in the tweet file")

# EXTRA CREDIT --- iii. Find the tweet(s) with the longest text message
lst_text = []
for line in content:
    newline = json.loads(line)
    if 'text' in newline:
        lst_text.append(newline.get('text'))
    else: 
        pass
for i in lst_text:
    if len(i) == 140: # twitter text character max is 140!
        print("This is one of the longest tweets at 140 characters:", i)



