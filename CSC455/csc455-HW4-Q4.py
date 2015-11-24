'''
1.	Write a python function that takes the name of a SQL table as parameter 
and then does the following:
Select all rows from that table (you can assume that the table already exists 
in SQLite) with all attributes from that table and 

output to a file a sequence 
of corresponding INSERT statements, one for each row from the table. Think of 
this as an exporting tool, since these INSERT statements could now be executed 
in Oracle (you do not need to actually do that).
'''
def generateInsertStatements(tablename):
    select = 'SELECT * FROM {};'.format(tablename)
    print(select)
    infile = open('Students.txt', 'r') # I used the Students.txt file as mentioned in the question which has headers
    content = infile.readlines()
    infile.close()
    for values in content:
        new = values.split("\n")
        for x in new:
                #print("INSERT INTO {} VALUES ({});".format(tablename, x))
            if x != '':
                with open("generateInsert.txt", "w") as out_file:
                    out_file.write("INSERT INTO {} VALUES ({});\n".format(tablename, x))
                with open("generateInsert.txt", "rt") as in_file:
                    text = in_file.read()    
                    print(text)
    out_file.close()
                
tablename = "Students"
generateInsertStatements(tablename)