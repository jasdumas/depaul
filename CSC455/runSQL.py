import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.connect('csc455_HW3.db')
c = conn.cursor()

# Open and read the file as a single buffer
fd = open('/Users/jasminedumas/Desktop/depaul/CSC455/ZooDatabase.sql', 'r')
# Read as a single document (not individual lines)
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';' which separates them)
sqlCommands = sqlFile.split(';')

# Execute every command from the input file (separated by ";")
for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    try:
        c.execute(command)
        print ("executed command: "+command)
    except OperationalError:
        print ("Command skipped: "+ command)

# For satement, print the results of the query above
for statement in sqlCommands:
    print (statement) # \n is the end of line symbol
len(sqlCommands)

c.close()
conn.commit()
conn.close()
