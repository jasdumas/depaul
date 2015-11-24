# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:30:02 2015

@author: dgv359
"""

import sqlite3
import pandas

StudentTable = '''CREATE TABLE StudentTest
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
c = conn.cursor()

# Get rid of the student table if we already created it
c.execute("DROP TABLE IF EXISTS StudentTest") #change
# Create the table in StudentDatabase.db
c.execute(StudentTable)

c.execute("INSERT INTO StudentTest1 Values ('1', 'John', '2nd');")
c.execute("INSERT INTO StudentTest1 Values ('2', 'Jane', '3rd');")
c.execute("INSERT INTO StudentTest1 Values ('3', 'John2', '4th');")
c.execute("INSERT INTO StudentTest1 Values ('4', 'Jane2', '6th');")
c.execute("INSERT INTO StudentTest1 Values ('5', 'John3', '5th');")

rows = c.execute("SELECT * FROM StudentTest1").fetchall()
df = pandas.DataFrame(rows)

import pandas.io.sql

pandarows = pandas.io.sql.read_sql('select * from StudentTest1', conn)

pandas.io.sql.to_sql(df, 'StudentTest4', conn, if_exists='append')

rows = c.execute("SELECT * FROM StudentTest4").fetchall()
df4 = pandas.DataFrame(rows)

# keeps track of all of the sql that gets run in the db
describerows = c.execute("SELECT sql FROM sqlite_master").fetchall() 


conn.commit()
conn.close()
#

