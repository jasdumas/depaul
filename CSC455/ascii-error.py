# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:30:02 2015

@author: jasminedumas
"""

import sys
import re, sqlite3, json
import urllib.request as urllib
# open url link/text file
response = urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt")
# empty list
lines = []
lines2 = [] 
counter = 0
counter2 = 0
# for loop to write tweets to a file 
for i in range(5):  # number should be 500000
    # read each line/tweet in and specify utf8
    str_response = response.readline().decode("utf8")
    #create_txt_file = str_response.write()
    with open("tweetfinal.txt", "w", "utf8") as out_txt_file:
        out_txt_file.write(str_response)
    with open("tweetfinal.txt", "rt", "utf8") as in_txt_file:
        # open the error file back up and read contents            
        text = in_txt_file.read()    