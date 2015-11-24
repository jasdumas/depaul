# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:35:48 2015

@author: dgv359
"""
import re, sqlite3, json
import urllib.request as urllib


response = urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment5.txt")
str_response = response.readline().decode("utf8")
tDict = json.loads(str_response)
tDict['id'] # just for example purposes
DictT = {} # if you wanted to re-create the dictionary
DictT[tDict['id']] = tDict
DictT


#The easiest way to read only the number of lines that you want using urllib is as follows.
#I definitely recommend testing your code with a few lines before you run it on 500K rows.

####DISCLAIMER - Some users may be offended

lines = []
for i in range(20): # change number to 7000 for amount of tweets
    str_response = response.readline().decode("utf8")
    newLine = response.readline() # Read just one line# Read just one line
    lines.append(newLine)
    tDict = json.loads(str_response)
    print('For tweet #',i,' the id is : ',tDict['id'], ' and tweet text is: ',tDict['text'])

    print ("Read", len(lines), "lines")

# same process as above with a try and except for ValueError
# save eror to a file
# if the errors show up re-run the url-open line!!!!
for i in range(40):
    str_response = response.readline().decode("utf8")
    newLine = response.readline() # Read just one line# Read just one line
    lines.append(newLine)
    try:
        tDict = json.loads(str_response)
        print('For tweet #',i,' the id is : ',tDict['id'], ' and tweet text is: ',tDict['text'])
    except(ValueError):
        print('For tweet #',i,' Tweet is corrupted and it trew a ValueError ',ValueError)


# Ignore these 3 lines
response = urllib.urlopen('http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment5.txt')
count = 0
tweet_dict = {}



#########
# go back to slides
#########

# Regular expression practice
email = "Steve's password is 12345, Ana's password is DePaul9 and I think Chris' password is Chris."
regex5 = re.compile("[A-Z][a-z]+\'s? password is \w+")
for password in regex5.findall(email):
   print(password)

# parentheses around (\w+) returns just the password
regex6 = re.compile("[A-Z][a-z]+\'s? password is (\w+)")
for password in regex6.findall(email):
   print(password)

# manipulate the string password of interest
regex5.findall(email)
for password in regex6.findall(email):
   email = email.replace(password, 'REDACTED!')

## Autoincrement in SQLite3
conn = sqlite3.connect('TestDB.db')
c = conn.cursor()
c.execute("CREATE TABLE MyTable (f1 NUMBER, f2 VARCHAR(50))")
c.execute('INSERT INTO MyTable VALUES (100, "Hello")');
c.execute("SELECT rowid, f1, f2 FROM MyTable").fetchall()
#rowid is always there unless you specify autoincrement

c.execute("CREATE TABLE MyTable2 (ID INTEGER PRIMARY KEY AUTOINCREMENT, f1 NUMBER, f2 VARCHAR(50))")
c.execute("INSERT INTO MyTable2(f1,f2) VALUES (200, 'Test')");
c.execute("INSERT INTO MyTable2(f1,f2) VALUES (300, 'Test3')");

c.execute("SELECT * FROM MyTable2").fetchall()

c.execute("SELECT rowid, ID, f1, f2 FROM MyTable2").fetchall()
c.execute("DELETE FROM MyTable2 WHERE ID = 2");

c.execute("INSERT INTO MyTable2(f1,f2) VALUES (350, 'Test')");
c.execute("INSERT INTO MyTable2(f1,f2) VALUES (360, 'Test3')");

c.execute("SELECT rowid, ID, f1, f2 FROM MyTable2").fetchall()


c.execute("INSERT INTO MyTable2(id, f1,f2) VALUES (500, 300, 'Test3')");
c.execute("INSERT INTO MyTable2(f1,f2) VALUES (400, 'Test4')");

c.execute("INSERT INTO MyTable2(id, f1,f2) VALUES (2, 300, 'Test3')");

c.execute("SELECT rowid, ID, f1, f2 FROM MyTable2").fetchall()
c.execute("SELECT rowid, ID, f1, f2 FROM MyTable2 ORDER BY rowid DESC").fetchall()



#####
#visualization PyPlot
######

import matplotlib.pyplot as plt
import numpy
from numpy.random import randn

#pl
#create a new figure - create the canvas
fig = plt.figure()

# adding subplots
sp1 = fig.add_subplot(2,2,1) # 2, 2, 1 shape of subplot: 2 dim x 2 dim & subplot 1
sp1.plot(randn(30)) # plot random numbers
fig.set_size_inches(15, 10)

fig

sp2 = fig.add_subplot(2,2,2)
sp2.scatter(randn(20), randn(20))
sp2.scatter(randn(20), randn(20), color = 'r') # scatter red dots
sp2.scatter(randn(15), randn(15), color = 'b')
sp3 = fig.add_subplot(2,2,3)
sp3.hist(randn(40), bins=10, color='g')
#Defaults to reduce_C_function = numpy.mean
plt.plot([1.5, 3.5, -2, 1.6]) # uses the latest subplot in memory uses same shape/size


sp4 = fig.add_subplot(2,2,4)
t = numpy.arange(0, 3.0, 0.01)
s = numpy.cos(2*numpy.pi*t)
sp4.plot(t, s)
fig
sp4.annotate('Center!', xy = (1.5,0), xytext = (1.2, 0.5))
plt.plot(randn(20), color='purple', linestyle='dashed')
from pylab import rcParams # another library - allows you to play w/ figure size in memory
rcParams['figure.figsize'] = 15, 10
plt.plot(randn(20), color='purple', linestyle='dashed', marker = 'o')

fig.set_size_inches(30, 15)
fig.set_size_inches(15, 10)

# nest figures
figx = plt.figure(); subfig = figx.add_subplot(1,1,1); 
data = randn(20)
subfig.plot(data, 'k--', label = "Initial Plot")
subfig.plot(data, 'k-', drawstyle="steps-post", label = "Post-step drawing style")
subfig.legend(loc='upper right')
subfig.plot(data+2, 'k-.', drawstyle="steps-pre", label = "Pre-step drawing style", color ='green', linewidth=5)
figx.savefig("myfigure.png")
figx.savefig("myfig.pdf", bbox_inches='tight')


##pandas aggregation
import pandas

df = pandas.DataFrame({'city':['Chicago', 'Chicago', 'Boston', 'Portland', 'Portland', 'Portland'],
                              'state':['IL', 'IL', 'MA', 'ME', 'OR', 'ME'],
	 	       'data1': randn(6), 'data2': randn(6) })
df
# look at data grouped by city
x = df['data1'].groupby(df['city'])
x.max() # run right on top of df
x.mean()

df['data1'].groupby([df['state'], df['city']]).min()
df.groupby([df['state']]).mean()
df.groupby([df['state']]).count()

# pretty output
for gname, gvalue in df.groupby('city'):
    print ('GroupName \n', gname)
    print ('GroupVal  \n', gvalue)
    print ("-"*30) # creates separator

#Dynamic Groups

df.groupby( lambda x : x*x ).mean()
df.groupby( lambda x : x/2 ).mean()

df.groupby('city').mean().groupby(len).mean()

df.groupby(['city', 'state']).agg('mean')


## execution time
# can calculate program runtime / performance
import time
start = time.time() # beginning of loop
for i in range(100000): # 100K operations
   dummy = json.loads(str_response)
end = time.time() # end of loop
print ("Difference is ", (end-start), 'seconds')
print ("Performance : ", 100000/(end-start), ' operations per second ')


