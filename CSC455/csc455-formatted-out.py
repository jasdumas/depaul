# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 19:52:03 2015

@author: jasminedumas
"""

def commas2char(lst):
    for entry in lst:
        if entry[0:] >= 'a' and entry[0:] <= 'z': # if its a character string
            print("this is a name or grade: ", entry)
    



a = ['1', 'Jane', 'A-']