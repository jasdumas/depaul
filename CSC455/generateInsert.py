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

chars = []


def generateInsert(tablename, lst):
    for entry in lst:
        if entry[0:] <= '9' and entry[0:] > '-': # if its a number and not a symbol by values of letters and symbols
            val = entry
        else:                                    # all letters/grades
            chars.append("'{}'".format(entry))

    sqlInsert = "INSERT INTO {} VALUES ({}, {}, {});".format(tablename, val, chars[0], chars[1])
    return sqlInsert
    

print(generateInsert('Students', ['1', 'Jane', 'A-']))

