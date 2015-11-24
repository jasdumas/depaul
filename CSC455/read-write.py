# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:48:48 2015

@author: jasminedumas
"""

 Write a file
with open("test.txt", "wt") as out_file:
    out_file.write("This Text is going to out file\nLook at it and see!")

# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)

# Skip over header in a table
with open(fname) as f:
    next(f)
    for line in f:
        #do something
with open('Students.txt','r') as f, open("updated_Students.txt",'w') as f1:
    next(f) # skip header line
    for line in f:
        f1.write(line)
