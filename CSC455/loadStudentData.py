# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:49:16 2015

@author: dv
"""

# #
import sqlite3

StudentTable = '''CREATE TABLE Student
(
  ID VARCHAR(5),
  Name VARCHAR(25),
  Standing VARCHAR(8),  
  CONSTRAINT Student_PK
     PRIMARY KEY(ID)
); '''

# Open a connection to database
conn = sqlite3.connect("StudentDatabase.db")

# Request a cursor from the database
cursor = conn.cursor()

# Get rid of the student table if we already created it
cursor.execute("DROP TABLE IF EXISTS Student")
# Create the table in StudentDatabase.db
cursor.execute(StudentTable)

# Open file for reading
fd = open('Students.txt', 'r')
# Read all lines from the file into allLines variable
allLines = fd.readlines()
fd.close() # Close the file

# For each line in the file
for line in allLines:
    
    # convert "A,B,C\n" line into ["A", "B", "C"] list of values.
    valueList = line.strip().split(',')

    # Load the values into the student table
    # NOTE that NULL would be loaded as string "NULL". If you want to
    # load NULLs properly, you would have to express them as None
    # i.e. NOT [111,'NULL','Grad'] but [111,None,'Grad'] instead
    cursor.execute("INSERT INTO Student VALUES (?,?,?);", valueList)

# Check what we inserted into the table
allSelectedRows = cursor.execute("SELECT * FROM Student;").fetchall()

# For every row, print the results of the query above, separated by a tab
for eachRow in allSelectedRows:
    for value in eachRow:
        print (value, "\t",)
    print ("\n",) # \n is the end of line symbol
len(allSelectedRows)
# Finalize inserts and close the connection to the database
conn.commit()
conn.close()
#
#