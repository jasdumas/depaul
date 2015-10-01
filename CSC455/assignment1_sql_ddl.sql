/*
Part 2
Using your logical schema from Part1, write the necessary SQL DDL script to cre
ate the tables. Be sure to specify every primary key and every foreign key. You
can make reasonable assumptions regarding the attribute domains.

*/


DROP TABLE Authors;
CREATE TABLE Authors(
 Author_ID NUMBER(12),
 Author_Lastname VARCHAR(20),
 Author_Firstname VARCHAR(20),
 Author_birthday DATE,  -- '09-SEP-1947' formatted like this

 CONSTRAINT Auth_pk
  PRIMARY KEY(Author_ID)
);

DROP TABLE Publisher;
CREATE TABLE Publisher(
  Publisher_ID NUMBER(12),
  Publisher_Name VARCHAR(30),
  Publisher_address VARCHAR(30),

  CONSTRAINT pub_pk
   PRIMARY KEY(Publisher_ID)
);

DROP TABLE Book;
CREATE TABLE Book(
  ISBN VARCHAR(8), -- it has a dash in the number
  title VARCHAR(45),
  Publisher_Name NUMBER(12), -- also a FK

 CONSTRAINT book_id
  PRIMARY KEY(ISBN),

 CONSTRAINT book_fk
  FOREIGN KEY (Publisher_Name) -- have to be the same data type NUMBER
   REFERENCES Publisher(Publisher_ID)
);


-- Part 2.2 for SQL INSERT statements
DROP TABLE BookComplete;
CREATE TABLE BookComplete(
  Author_ID NUMBER(12),  -- Author who writes the book dictates ISBN and rank
  ISBN VARCHAR(8),
  Author_rank NUMBER(1),

  CONSTRAINT BC_pk
   PRIMARY KEY (ISBN),

  CONSTRAINT BC_fk
   FOREIGN KEY (ISBN)
    REFERENCES Book(ISBN),

  CONSTRAINT BC2_fk
   FOREIGN KEY (Author_ID)
    REFERENCES Authors(Author_ID)

);
