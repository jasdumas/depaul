
chars = []


def generateInsert(tablename, lst):
    for entry in lst:
        if entry[0:] <= '9' and entry[0:] > '-': # if its a number and not a symbol by values of letters and symbols
            val = entry
        else:                                    # all letters/grades
            chars.append("'{}'".format(entry))

    sqlInsert = "INSERT INTO {} VALUES ({}, {} ,{} );".format(tablename, val, chars[0], chars[1])
    return sqlInsert
    

print(generateInsert('Students', ['1', 'Jane', 'A-']))

