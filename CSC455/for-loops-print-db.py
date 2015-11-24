# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:31:05 2015

@author: jasminedumas
"""

one = ['apple', 'orange']

two = ['grape', 'kiwi', "jasmine", "jas", "jenna", "Fiona"]

three = [("jasmine", "jenna"), ("Fiona", "Bailey")]

#for i in one: 
#    print(" {} |".format(i))
counter = 0   
for tup in three:
    for i in tup:
        if i in two:
            print("yes")
            counter += 1
        if i == "Fiona":
            pass
            #print("small dog")
            #print(" {} |\n".format(i))
            i = "trouble"
        if i == "Bailey":
            pass
            #print("big dog")
            #print(" {} |\n".format(i))
        print(" {} |\n".format(i))
print(counter)


trial = ('471803285742313472','Brendan Robinson','Robinson_19_','Instagram: Robinson_19_',72)
trial2 = ('471803285742313472','Jasmine Dumas','Jasmine Dumas','y',272)
for i in trial2:
    if trial2[1] in trial2[2:3]:
        #print(True)
        a = "True"
    else:
        pass
        #print(False)
        a = "False"
print(trial2 + (a,))


a = ('2',)
b = 'z'
new = a + (b,)



g = ('471803868775723008', 'Point', '-23.77122', '-46.677161')
i = ('-23.77122', '-46.677161','Point')
for item in i:
    if type(item) == type(float('14.55554')):
        pass
        #item_new = round(float(item), 4)
        print("this is", round(float(item), 4), "old item", item)
    else:
        pass
        print("fuck")
        
        
def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)
    
    
    
    