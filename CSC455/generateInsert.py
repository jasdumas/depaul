'''
Part 2.3

Write a python function that is going to generate and return a SQL INSERT
statement given a table name and value list as parameters. For example,
generateInsert('Students', ['1', 'Jane', 'A-']) should return
“INSERT INTO Students VALUES (1, Jane, A-);”. It would be even better,
but not required if your function returned the more proper
“INSERT INTO Students VALUES (1, 'Jane', 'A-');” (i.e., put quotes around string
s, but not numbers).

'''

def generateInsert(tablename, vallist):
    
    a = "INSERT INTO {} VALUES ({}, '{}', '{}');".format(tablename, vallist[0], vallist[1], vallist[2])
    return a

print(generateInsert('Students', ['1', 'Jane', 'A-']))
