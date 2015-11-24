# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:01:07 2015

@author: jasminedumas
"""

def randstr(stringid):
    lst = []
    lst2 = []
    for x in stringid:
        #print(x)
        lst.append(chr(ord(x)+1))
    lst2.append(''.join(lst))
    #print(''.join(lst))
    print(lst2)   
    
    

randstr('454503287638734024')
randstr('471803233333333300')
randstr('471803444442333332')
randstr('9999999')  # the next increment up from 9 is :
randstr('@jasdumas')
randstr('@jennamdaly')