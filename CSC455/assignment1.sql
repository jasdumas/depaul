DROP TABLE Authors;
CREATE TABLE Authors(
 Author_ID NUMBER(12) PRIMARY KEY,
 Author_Lastname VARCHAR(20),
 Author_Firstname VARCHAR(20),
 Author_birthday DATE
);

SELECT * FROM Authors;

INSERT INTO Authors(
  Author_ID, Author_Lastname, Author_Firstname, Author_birthday
) VALUES ('2','King', 'Stephen', '09-SEP-1947');
  



SELECT * FROM Authors;


INSERT INTO Authors(
Author_ID, Author_Lastname, Author_Firstname, Author_birthday
) VALUES ('4', 'Asimov', 'Isaac', '02-JAN-1920');

SELECT * FROM Authors;

DROP TABLE Publisher;
CREATE TABLE Publisher(
  Publisher_ID NUMBER(12) PRIMARY KEY, -- also a FK
  Publisher_Name VARCHAR(30),
  Publisher_address VARCHAR(30)
);
  
SELECT * FROM Publisher;

INSERT INTO Publisher(
  Publisher_ID, Publisher_Name, Publisher_address
) VALUES ('17', 'Bloomsbury Publishing', 'London Borough of Camden');
INSERT INTO Publisher(
  Publisher_ID, Publisher_Name, Publisher_address
) VALUES('18', 'Arthur A. Levine Books', 'New York City');

SELECT * FROM Publisher;

DROP TABLE Book;
CREATE TABLE Book(
  ISBN NUMBER(8) PRIMARY KEY, 
  title VARCHAR(45),
  Publisher_Name VARCHAR(30), -- also a FK
  CONSTRAINT Publisher_Name FOREIGN KEY (Publisher_ID)
);


DROP TABLE Book;
CREATE TABLE Book(
  ISBN NUMBER(8),
  title VARCHAR(45),
  Publisher_Name VARCHAR(30), -- also a FK

 CONSTRAINT book_id
  PRIMARY KEY(ISBN)

 CONSTRAINT Publisher_Name
  FOREIGN KEY Publisher(Publisher_ID)
);


DROP TABLE Book;

CREATE TABLE Book(
  ISBN VARCHAR(8),
  title VARCHAR(45),
  Publisher_Name VARCHAR(30), -- also a FK

 CONSTRAINT book_id
  PRIMARY KEY(ISBN)
);

INSERT INTO Book(
  ISBN, title, Publisher_Name
) VALUES ('1111-111','Databases from outer space', '17');

INSERT INTO Book(
  ISBN, title, Publisher_Name
) VALUES ('2222-222', 'Dark SQL', '17');

INSERT INTO Book(
  ISBN, title, Publisher_Name
) VALUES ('3333-333', 'The night of the living databases', '18');

SELECT * FROM Book;


DROP TABLE Book;
CREATE TABLE Book(
  ISBN VARCHAR(8) PRIMARY KEY,
  title VARCHAR(45),
  Publisher_Name VARCHAR(30) FOREIGN KEY Publisher(Publisher_ID) -- also a FK

  
);

DROP TABLE Book;
CREATE TABLE Book(
  ISBN VARCHAR(8), -- it has a dash in the number
  title VARCHAR(45),
  Publisher_Name VARCHAR(30), -- also a FK

 CONSTRAINT book_id
  PRIMARY KEY(ISBN),

 CONSTRAINT book_fk
  FOREIGN KEY (Publisher_Name)
   REFERENCES Publisher(Publisher_ID)
);



DROP TABLE Book;
CREATE TABLE Book(
  ISBN VARCHAR(8), -- it has a dash in the number
  title VARCHAR(45),
  Publisher_ID VARCHAR(30), -- also a FK

 CONSTRAINT book_id
  PRIMARY KEY(ISBN),

 CONSTRAINT book_fk
  FOREIGN KEY (Publisher_ID)
   REFERENCES Publisher(Publisher_ID)
);


CREATE TABLE Book(
  ISBN VARCHAR(8), -- it has a dash in the number
  title VARCHAR(45),
  Publisher_Name NUMBER(12), -- also a FK

 CONSTRAINT book_id
  PRIMARY KEY(ISBN),

 CONSTRAINT book_fk
  FOREIGN KEY (Publisher_Name)
   REFERENCES Publisher(Publisher_ID)
);

SELECT * FROM Book;


