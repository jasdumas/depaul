-- Drop all the tables to clean up
DROP TABLE Animal;

-- ACategory: Animal category 'common', 'rare', 'exotic'.  May be NULL
-- TimeToFeed: Time it takes to feed the animal (hours)
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR2(30) NOT NULL,
  ACategory VARCHAR2(18),
  
  TimeToFeed NUMBER(4,2),  
  
  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);


INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);
INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);
INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);
INSERT INTO Animal VALUES(4, 'Grizzly bear', NULL, 2.5);
INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);
INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);
INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.75);
INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);
INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.25);
INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);
INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.5);


--Queries
SELECT AName FROM Animal
 WHERE TIMETOFEED < 1.5;
 
SELECT AName, TimeToFeed FROM Animal
 WHERE ACATEGORY = 'rare'
  ORDER BY TimeToFeed DESC;
  
SELECT AName, ACategory FROM Animal
 WHERE AName LIKE '%bear';
 
SELECT AName FROM Animal
WHERE ACATEGORY IS NULL;

SELECT * FROM Animal
WHERE TIMETOFEED >=1 and TIMETOFEED <= 2.5;

SELECT AName FROM Animal
WHERE AName LIKE '%tiger' and ACategory <> 'common';

SELECT MIN(TIMETOFEED), MAX(TIMETOFEED) From Animal;

SELECT AVG(TIMETOFEED) FROM Animal
WHERE ACATEGORY = 'rare';

SELECT * from Animal
 WHERE AID < 10 and TIMETOFEED > 2;