
/*
	SQL Examples
	Alexander Rasin, Dragos Visan
	CSC 455 Fall 2014, Fall 2015
*/

-- get rid of existing tables
DROP TABLE Transaction;
DROP TABLE Stores;

-- create the new tables, each with primary keys
CREATE TABLE Stores(
        StoresID   NUMBER,
        City    VARCHAR2(20) NOT NULL,
        State  CHAR(2) NOT NULL,
      
      CONSTRAINT Stores_ID
            PRIMARY KEY (StoresID)
);

CREATE TABLE Transaction(
        StoresID   NUMBER,
	TransID  NUMBER,
	TDate       DATE,
        Amount  NUMBER(*, 2),

      CONSTRAINT DateCheck
           Check (TDate > To_Date('01-Jan-2010')),
      CONSTRAINT AmountCheck
           Check (Amount > 0.00),
      CONSTRAINT Transaction_ID
           PRIMARY KEY (StoresID, TransID),
      CONSTRAINT Transaction_FK1
           FOREIGN KEY (StoresID)
           REFERENCES Stores(StoresID)
);

-- insert data...
INSERT INTO Stores VALUES  (100, 'Chicago', 'IL');
INSERT INTO Stores VALUES  (200, 'Chicago', 'IL');
INSERT INTO Stores VALUES  (300, 'Schaumburg', 'IL');
INSERT INTO Stores VALUES  (400, 'Boston', 'MA');
INSERT INTO Stores VALUES  (500, 'Boston', 'MA');
INSERT INTO Stores VALUES  (600, 'Portland', 'ME');

INSERT INTO Transaction Values(100, 1, '10-Oct-2011', 100.00);
INSERT INTO Transaction Values(100, 2, '11-Oct-2011', 120.00);
INSERT INTO Transaction Values(200, 1, '11-Oct-2011', 50.00);
INSERT INTO Transaction Values(200, 2, '11-Oct-2011', 70.00);
INSERT INTO Transaction Values(300, 1, '12-Oct-2011', 20.00);
INSERT INTO Transaction Values(400, 1, '10-Oct-2011', 10.00);

INSERT INTO Transaction Values(400, 2, '11-Oct-2011', 20.00);
INSERT INTO Transaction Values(400, 3, '12-Oct-2011', 30.00);
INSERT INTO Transaction Values(500, 1, '10-Oct-2011', 10.00);
INSERT INTO Transaction Values(500, 2, '10-Oct-2011', 110.00);
INSERT INTO Transaction Values(500, 3, '11-Oct-2011', 90.00);
INSERT INTO Transaction Values(600, 1, '11-Oct-2011', 300.00);

INSERT INTO Transaction Values(100, 1, '10-Oct-2011', 100.00);
INSERT INTO Transaction Values(200, 1, '11-Oct-2011', 50.00);
INSERT INTO Transaction Values(300, 1, '12-Oct-2011', NULL);
INSERT INTO Transaction Values(400, 1, '10-Oct-2011', 10.00);
INSERT INTO Transaction Values(500, 1, '10-Oct-2011', 10.00);
INSERT INTO Transaction Values(600, 1, '11-Oct-2011', NULL);

SELECT Amount, TDate, TransID
FROM Transaction
ORDER BY Amount;

SELECT TDate, Amount
FROM Transaction
WHERE Amount >=20
ORDER BY TDate DESC, Amount ASC;

SELECT SYSDATE FROM Dual;

SELECT * from Transaction 
   WHERE TDate = to_date(SYSDATE - (365*3) + 3);


SELECT COUNT(*) FROM Transaction;
SELECT COUNT(*) FROM Stores;

SELECT COUNT(State) FROM Stores;
SELECT COUNT(DISTINCT State) FROM Stores;

SELECT COUNT(Amount) FROM Transaction;

SELECT SUM(*)
FROM Transaction; -- Cannot be done

SELECT SUM(Amount) FROM Transaction;
SELECT MIN(Amount) FROM Transaction;

SELECT SUM(Amount)
FROM Transaction
WHERE Amount <= 20 OR Amount >= 100;

SELECT AVG(Amount)
FROM Transaction;

SELECT AVG(Amount)
FROM Transaction
WHERE TDate = to_date('11-Oct-2011');

SELECT SUM(Amount)/COUNT(Amount)
FROM Transaction;

  SELECT MAX(Amount)
  FROM Transaction
  WHERE Amount < 55;


  SELECT state, COUNT(StoresID)
  FROM Stores
  GROUP BY state;

  SELECT state, COUNT(DISTINCT city)
  FROM Stores
  GROUP BY state;

  SELECT state, city, COUNT(StoresID)
  FROM Stores
  GROUP BY state, city;


SELECT TDate, SUM(Amount)
  FROM Transaction
  GROUP BY TDate;

  SELECT StoresID, MAX(Amount)
  FROM Transaction
  GROUP BY StoresID;

 SELECT StoresID, MAX(Amount)
  FROM Transaction
  GROUP BY StoresID
  ORDER BY StoresID;

SELECT StoresID, SUM(Amount)
  FROM Transaction;
   (Can’t do that!)

  SELECT StoresID, 0.5*MIN(Amount), 1.5*MAX(Amount)
  FROM Transaction
  GROUP BY StoresID
  ORDER BY StoresID DESC;


SELECT TDate, SUM(Amount)
  FROM Transaction
  WHERE SUM(Amount) > 200 -- Cannot do that!
  GROUP BY TDate; 

 SELECT TDate, SUM(Amount)
  FROM Transaction
  GROUP BY TDate
  HAVING SUM(Amount) > 200;


SELECT * from Stores, Transaction;
SELECT * from Stores, Transaction, Student;


-- create tables
drop table enrolled;
drop table  course;
drop table student;

create table student (
  LastName      varchar(40),
  FirstName     varchar(40),
  StudentID           number(5),
  SSN           number(9),
  Career        varchar(4),
  ProgramName       varchar(10),
  City          varchar(40),
  Started       number(4),
  
  primary key (StudentID),
  unique(SSN)
);

create table course (
  CID   number(4),
  CourseName    varchar(40),
  Department    varchar(4),
  CourseNr       char(3),

  primary key (CID)
);

create table enrolled (
  StudentID     number(5),
  CourseID      number(4),
  Quarter       varchar(6),
  Year          number(4),
  
  primary key (StudentID, CourseID),
  foreign key (StudentID) references student(StudentID),
  foreign key (CourseID) references course(CID)
); 


insert into student
    values ( 'Brennigan', 'Marcus', 90421, 987654321, 'UGRD', 'COMP-GPH', 'Evanston', 2001 );
insert into student
    values ( 'Patel', 'Deepa', 14662, null, 'GRD', 'COMP-SCI', 'Evanston', 2003 );
insert into student
    values ( 'Snowdon', 'Jonathan', 08871, 123123123, 'GRD', 'INFO-SYS', 'Springfield', 2005 );
insert into student
    values ( 'Starck', 'Jason', 19992, 789789789, 'UGRD', 'INFO-SYS', 'Springfield', 2003 );
insert into student
    values ( 'Johnson', 'Peter', 32105, 123456789, 'UGRD', 'COMP-SCI', 'Chicago', 2004 );
insert into student
    values ( 'Winter', 'Abigail', 11035, 111111111, 'GRD', 'PHD', 'Chicago', 2003 );
insert into student
    values ( 'Patel', 'Prakash', 75234, null, 'UGRD', 'COMP-SCI', 'Chicago', 2001 );
insert into student
    values ( 'Snowdon', 'Jennifer', 93321, 321321321, 'GRD', 'COMP-SCI', 'Springfield', 2004 );

insert into course
    values ( 1020, 'Theory of Computation', 'CSC', 489);
insert into course
    values ( 1092, 'Cryptography', 'CSC', 440);
insert into course
    values ( 3201, 'Data Analysis', 'IT', 223);
insert into course
    values ( 9219, 'Desktop Databases', 'IT', 240);
insert into course
    values ( 3111, 'Theory of Computation', 'CSC', 389);
insert into course
    values ( 8772, 'Survey of Computer Graphics', 'GPH', 425);
insert into course
    values ( 2987, 'Topics in Digital Cinema', 'DC', 270);
    
insert into enrolled
    values (11035, 1020, 'Fall', 2005);
insert into enrolled
    values (11035, 1092, 'Fall', 2005);
insert into enrolled
    values (75234, 3201, 'Winter', 2006);
insert into enrolled
    values (08871, 1092, 'Fall', 2005);
insert into enrolled
    values (90421, 8772, 'Spring', 2006);
insert into enrolled
    values (90421, 2987, 'Spring', 2006);
    

SELECT * FROM Student, Enrolled;

SELECT * FROM
Student, Enrolled
WHERE Student.StudentID = Enrolled.StudentID;

SELECT * FROM
Student JOIN Enrolled ON Student.StudentID = Enrolled.StudentID;

SELECT * FROM
Student NATURAL JOIN Enrolled;

SELECT * FROM
Student INNER JOIN Enrolled ON Student.StudentID = Enrolled.StudentID;

SELECT * FROM
Student LEFT OUTER JOIN Enrolled ON Student.StudentID = Enrolled.StudentID;

-- Can also do this
SELECT * FROM
Student LEFT JOIN Enrolled ON Student.StudentID = Enrolled.StudentID;

SELECT * FROM
Student RIGHT OUTER JOIN Enrolled ON Student.StudentID = Enrolled.StudentID;

SELECT * FROM
Enrolled RIGHT OUTER JOIN Course ON CourseID = CID;

SELECT *
FROM Enrolled FULL OUTER JOIN Student ON Enrolled.StudentID = Student.StudentID;


SELECT FirstName, LastName, Year, Started
FROM enrolled, student
WHERE Year <> Started;

---


DROP TABLE Employee;
CREATE TABLE Employee(
  EmpID NUMBER(7),
  Name  VARCHAR2(20),
  Position VARCHAR2(50),
  Supervisor NUMBER(7),

  CONSTRAINT EmpPK
    PRIMARY KEY(EmpID));

ALTER TABLE Employee
ADD CONSTRAINT SupFK 
FOREIGN KEY (Supervisor)
REFERENCES Employee(EmpID);

ALTER TABLE Employee DROP CONSTRAINT SupFK;

INSERT INTO Employee VALUES(1, 'Lucia', 'Associate Dean', 4);
INSERT INTO Employee VALUES(2, 'Eric', 'Faculty', 1);
INSERT INTO Employee VALUES(3, 'Alex', 'Faculty', 1);
INSERT INTO Employee VALUES(4, 'David', 'Dean', NULL);
INSERT INTO Employee VALUES(5, 'Ted', 'MS Student', 3);

SELECT * FROM Employee;

SELECT e2.Name, ' supervised by  ', e1.Name
FROM Employee e1, Employee e2
WHERE e1.EmpID = e2.supervisor;

-- Outer join?
SELECT e2.Name, ' supervised by  ', e1.Name
FROM Employee e1 LEFT OUTER JOIN Employee e2 
on e1.EmpID = e2.supervisor;

-------

DROP TABLE Enrolled;
DROP TABLE Student;
DROP TABLE Course;
-- Course/Student Example

CREATE TABLE Student
(
  ID VARCHAR2(5),
  Name VARCHAR2(25) NOT NULL,
  Standing VARCHAR2(8),
    
  CONSTRAINT Student_PK
     PRIMARY KEY(ID)
);

CREATE TABLE Course
(
  CourseID VARCHAR2(15),
  Name VARCHAR2(50) UNIQUE,
  Credits NUMBER(*,0) CHECK (Credits > 0),
  
  CONSTRAINT Course_PK
     PRIMARY KEY( CourseID)
);

CREATE TABLE Enrolled
(
  StudentID VARCHAR2(5),
  CourseID VARCHAR2(15),
  Enrolled DATE,

  CONSTRAINT En_PK
     PRIMARY KEY(CourseID, StudentID),
  
  CONSTRAINT En_FK1
     FOREIGN KEY (CourseID)
       REFERENCES Course(CourseID),
       
  CONSTRAINT En_FK2
     FOREIGN KEY (StudentID)
       REFERENCES Student(ID)
);

INSERT INTO Course VALUES ('CSC211', 'Intro to Java I', 4);
INSERT INTO Course VALUES ('IT130', 'The Internet and the Web', 2);
INSERT INTO Course VALUES ('CSC452', 'Database Design II', 4);
INSERT INTO Course VALUES ('CSC451', 'Database Design', 4);

INSERT INTO Student VALUES ('12345', 'Paul K', 'Grad');
INSERT INTO Student VALUES ('23456', 'Larry P', 'Grad');
INSERT INTO Student VALUES ('34567', 'Ana B', 'Ugrad');
INSERT INTO Student VALUES ('45678', 'Mary Y', 'Grad');
INSERT INTO Student VALUES ('56789', 'Pat B', 'Ugrad');
INSERT INTO Student VALUES ('66789', 'Pat B', 'Grad');

INSERT INTO Enrolled VALUES('12345', 'CSC211', '01-Jan-2011');
INSERT INTO Enrolled VALUES('12345', 'CSC451', '02-Jan-2011');

INSERT INTO Enrolled VALUES('23456', 'IT130', '03-Jan-2011');

INSERT INTO Enrolled VALUES('34567', 'CSC211', '06-Jan-2011');
INSERT INTO Enrolled VALUES('34567', 'IT130', '07-Jan-2011');
INSERT INTO Enrolled VALUES('34567', 'CSC451', '11-Jan-2011');

INSERT INTO Enrolled VALUES('45678', 'IT130', '02-Jan-2011');
INSERT INTO Enrolled VALUES('45678', 'CSC211', '02-Jan-2011');


SELECT Name
FROM Course;

SELECT SUM(Credits)
FROM Course;

SELECT Standing, COUNT(*)
FROM Student
GROUP BY Standing;

SELECT Name, COUNT(CourseID)
FROM Student stu, Enrolled enr
WHERE stu.ID = StudentID     --this works due to ambiguity solved by at least one  attribute name referencing the parent table, not good practice though!
GROUP BY Name
HAVING COUNT(CourseID)>=2;

/*Slide 45
Find all students that are not currently taking any courses:
*/


SELECT *--Name, COUNT(CourseID)
FROM Student, Enrolled
WHERE Student.ID = Enrolled.StudentID;
GROUP BY Name
HAVING COUNT(CourseID)=0;
/*Slide 45
Not going to work because the count 0 will never be displayed 
since the Equi-Join does not list the tuples that have no match.

For this, you need a LEFT OUTER JOIN below so that your students with no enrollment matching tuples show
in other words, Need to find the tuples absent from join
slide 46
*/

SELECT Name, Enrolled.COURSEID
FROM Student LEFT OUTER JOIN Enrolled
ON (Student.ID = StudentID)
WHERE CourseID IS NULL;

/*Slide 47
List all courses IDs and the number of students enrolled
*/

SELECT Course.CourseID, Count(StudentID)
FROM Course, Enrolled
WHERE Course.CourseID = Enrolled.CourseID
GROUP BY Course.CourseID;

/*Slide 48
List all course names and the number of students enrolled, ordered by popularity
*/

SELECT Name, Count(StudentID) as Enrolled
FROM Course, Enrolled
WHERE Course.CourseID = Enrolled.CourseID
GROUP BY Name
ORDER BY Enrolled DESC;

/*Slide 49
List students and the course names they are enrolled in
*/

SELECT Student.Name, Course.Name
FROM Course, Enrolled, Student
WHERE Student.ID = Enrolled.StudentID AND Enrolled.CourseID = Course.CourseID
ORDER BY Student.Name;
