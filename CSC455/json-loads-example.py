# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:51:57 2015

@author: dgv359
"""


import json

#based on hw2 example loadStudentData.py
fd = open('jsonexample.txt', 'r', encoding='utf8') #similar to past reads for hw2, but we are encoding the bytes

allLines = fd.readline().split('somedelimiter') #splits the lines on a delimiter and creates strings for each line 
type(allLines[0]) #check type of first list item, making sure it is a string so that json can load it

fd.close()

# For each line in the file
for line in allLines:
    jsonobject = json.loads(line)
    print (jsonobject['essentials'])
    print (jsonobject['answers']['lifetheuniverseandeverything'],'\n')


