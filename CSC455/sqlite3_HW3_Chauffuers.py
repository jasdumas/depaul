import sqlite3

RecordTable = '''CREATE TABLE RecordNumber(
 License NUMBER(6),
 Renewed DATE, --MMYYYY
 Status VARCHAR(10),
 Status_date DATE, --MMDDYYYY
 Driver_type CHAR(15),
 License_type VARCHAR(15),
 Original DATE, --MMDDYYYY
 Name CHAR(30),
 Sex CHAR(7),
 Chauffeur_city CHAR(15),
 Record_Num VARCHAR(12) NOT NULL UNIQUE,

 CONSTRAINT Rec_pk
  PRIMARY KEY(Record_Num)
);
'''
#
# Open a connection to database
conn = sqlite3.connect("publicchauffeur.db")

# Request a cursor from the database
cursor = conn.cursor()

# Get rid of the tables if we already created it
cursor.execute('DROP TABLE IF EXISTS RecordNumber')

# Create the table in publicchauffeur.db
cursor.execute(RecordTable)

# Open file for reading
fd = open('/Users/jasminedumas/Desktop/depaul/CSC455/Public_Chauffeurs_Short_hw3.csv', 'r')

# Read all lines from the file into allLines variable
allLines = fd.readlines()
fd.close() # Close the file

# For each line in the file
for line in allLines[1:]:   # that subset excludes the column names in row 0
    for word2 in line:  # replaces all "NULL"s with None or empty null string
        if word2 is "NULL" or "":
            word2.replace("NULL", None)  
    # convert "A,B,C\n" line into ["A", "B", "C"] list of values.
    valueList = line.strip().split(",")

    # Load the values into the RecordNumber table (11 columns)
    cursor.execute("INSERT OR IGNORE INTO RecordNumber VALUES (?,?,?,?,?,?,?,?,?,?,?);", 
    (valueList[0], valueList[1], valueList[2], valueList[3], valueList[4], 
    valueList[5], valueList[6], valueList[7], valueList[8], valueList[9], valueList[11]))


# Check what we inserted into the table
allSelectedRows = cursor.execute("SELECT * FROM RecordNumber;").fetchall()

# For every row, print the results of the query above, separated by a tab
for eachRow in allSelectedRows:
    for value in eachRow:
        print (value, "\t",)
    print ("\n",) # \n is the end of line symbol
len(allSelectedRows)
# Finalize inserts and close the connection to the database
conn.commit()
conn.close()

#######################
# Table 2
#######################
ChauffeurTable = '''CREATE TABLE ChauffeurCity(
  Chauffeur_city CHAR(15),
  Chauffeur_state CHAR(15),

  CONSTRAINT Chf_pk
    PRIMARY KEY(Chauffeur_city),

  CONSTRAINT Chf_fk
    FOREIGN KEY (Chauffeur_city)
      REFERENCES RecordNumber(Chauffeur_city)
);
'''

# Open a connection to database
conn2 = sqlite3.connect("publicchauffeur.db")

# Request a cursor from the database
cursor2 = conn2.cursor()

# Get rid of the tables if we already created it
cursor2.execute('DROP TABLE IF EXISTS ChauffeurCity')

# Create the table in publicchauffeur.db
cursor2.execute(ChauffeurTable)

# Open file for reading
fd2 = open('/Users/jasminedumas/Desktop/depaul/CSC455/Public_Chauffeurs_Short_hw3.csv', 'r')

# Read all lines from the file into allLines variable
allLines2 = fd2.readlines()
fd2.close() # Close the file

# put in a subset of only city and state
# For each line in the file 
for line2 in allLines2[1:]:   # that subset excludes the column names in row 0
    for word in line2:
        if word is "NULL":
            word.replace("NULL", None)   
    
    # convert "A,B,C\n" line into ["A", "B", "C"] list of values.
    valueList2 = line2.strip().split(",")

    # Load the values into the ChauffeurCity table 
    # (2 columns in the 9 through 11 index in the csv file)
    cursor2.execute("INSERT OR IGNORE INTO ChauffeurCity VALUES (?,?);", valueList2[9:11])


# Check what we inserted into the table
allSelectedRows2 = cursor2.execute("SELECT * FROM ChauffeurCity;").fetchall()

# For every row, print the results of the query above, separated by a tab
for eachRow in allSelectedRows2:
    for value in eachRow:
        print (value, "\t",)
    print ("\n",) # \n is the end of line symbol
len(allSelectedRows2)
# Finalize inserts and close the connection to the database
conn2.commit()
conn2.close()
