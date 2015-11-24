"""
a.	Write python code to compute the answer from 3-e without using SQL, i.e., 
write code that is going to read data from the input file and answer the same 
question (find how many tweets have a “retweet_count” of at least 5).
"""

import json
filename = '/Users/jasminedumas/Desktop/depaul/CSC455/Assignment4.txt'
infile = open(filename, 'r', encoding='utf8')
content = infile.read()
lst = []
for line in content.split('EndOfTweet'):
    newline = json.loads(line)
    if 'retweet_count' in newline:
        lst.append(newline.get(u'retweet_count'))
    else: 
        lst.append(newline.get(u'retweeted_status''retweet_count'))

counter = 0
for i in lst:
    if i >= 5:
        counter += 1
print("This is the amount of tweets that have atleast 5 retweets: ",counter) 

