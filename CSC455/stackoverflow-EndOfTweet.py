# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:09:45 2015

@author: jasminedumas
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

counter = 0
for i in lst:
    if i >= 5:
        counter += 1
print("This is the amount of tweets that have atleast 5 retweets: ",counter) 

