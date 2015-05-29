# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:33:52 2015

@author: jasmine.dumas
"""

def removeduplicates(sentence):
    sentence = sentence.split()    
    lst = []
    
    for i in sentence:
        if i not in lst:
            lst.append(i)
    print(lst)
    
        
removeduplicates("this is a example example sentence")
    
