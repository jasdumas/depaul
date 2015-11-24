# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 06:57:58 2015

@author: dgv359

"""

from urllib.request import urlopen
url = urlopen("http://www.google.com/")
pw = url.read()
print (pw)


import urllib.request
webFD = urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/tweet_data.txt")
#webFD.readlines()

tweets= webFD.readlines() #.decode('UTF-8').split('-----')
cnt = 0      
for line in tweets:
    print("count ", cnt,"\r\n", line)
    cnt += 1
tweets[22]

webFD.close()

