
DROP TABLE Handles;
DROP TABLE Animal;
DROP TABLE ZooKeeper;

CREATE TABLE ZooKeeper
(
  ZID        NUMBER(3,0),
  ZName       VARCHAR2(25) NOT NULL,
  HourlyRate NUMBER(6, 2) NOT NULL,
  
  CONSTRAINT ZooKeeper_PK
     PRIMARY KEY(ZID)
);

CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR(30) NOT NULL,
  ACategory VARCHAR(18),  
  TimeToFeed NUMBER(4,2),  
  
  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);


CREATE TABLE Handles
(
  ZooKeepID      NUMBER(3,0),
  AnimalID     NUMBER(3,0),
    Assigned     DATE,
  
  CONSTRAINT Handles_PK
    PRIMARY KEY(ZooKeepID, AnimalID),
    
  CONSTRAINT Handles_FK1
    FOREIGN KEY(ZooKeepID)
      REFERENCES ZooKeeper(ZID),
      
  CONSTRAINT Handles_FK2
    FOREIGN KEY(AnimalID)
      REFERENCES Animal(AID)
);

INSERT INTO ZooKeeper VALUES (1, 'Jim Carrey', 500);
INSERT INTO ZooKeeper VALUES (2, 'Tina Fey', 350);  
INSERT INTO ZooKeeper VALUES (3, 'Rob Schneider', 250);
  
INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);
INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);
INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);
INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);
INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);
INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);
INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.5);
INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);
INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.25);
INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);
INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.5);

INSERT INTO Handles VALUES(1, 1, '01-Jan-2000');
INSERT INTO Handles VALUES(1, 2, '02-Jan-2000');
INSERT INTO Handles VALUES(1, 10, '01-Jan-2000');
INSERT INTO Handles VALUES(2, 3, '02-Jan-2000');
INSERT INTO Handles VALUES(2, 4, '04-Jan-2000');
INSERT INTO Handles VALUES(2, 5, '03-Jan-2000');
INSERT INTO Handles VALUES(3, 7, '01-Jan-2000');
INSERT INTO Handles VALUES(3, 8, '03-Jan-2000');
INSERT INTO Handles VALUES(3, 9, '05-Jan-2000');
INSERT INTO Handles Values(3, 10,'04-Jan-2000');

/*   ******  Simple interview practice (8-14-16) *******         */

/* general selects by numeric criteria */
select * from Handles;

select * from Handles 
where ZOOKEEPID >= 2;

select * from Handles
where ZOOKEEPID >= 2 AND ANIMALID >= 5;

/* general selects by string criteria */
select AName from animal
where ACATEGORY = 'exotic';

/* general selects by wild card string match criteria */
select AName as Animal_Name from Animal
where AName like 'L%';

select AName as Animam_Name from Animal
where AName like 'G%';

select timetofeed, AName as Animam_Name from Animal
where AName like '%bear%' and TIMETOFEED < 2;

/* aggregates - counts */
select count(ACategory), ACategory as cnttype from Animal
group by ACategory;

/* aggregates - range */
select max(timetofeed), min(timetofeed) from animal;

select distinct(ACategory) from animal;




/*   ********************         */
SELECT Animal.Aname, Handles.ZOOKEEPID
FROM Animal
INNER JOIN Handles
ON Animal.AID = Handles.AnimalID;

SELECT Animal.ANAME, Handles.ZOOKEEPID
FROM Animal
FULL OUTER JOIN Handles
ON AID = Handles.ANIMALID
order by Handles.ZOOKEEPID DESC;

SELECT Animal.ANAME, Zookeeper.Zname, (Zookeeper.HourlyRate*Animal.TIMETOFEED) as payout
FROM Animal
INNER JOIN Handles
JOIN Zookeeper ON Handles.ZOOKEEPID = Zookeeper.ZID
ON Animal.AID = Handles.ANIMALID;


SELECT Zookeeper.Zname, sum(Animal.TIMETOFEED) as total_time
FROM Animal
INNER JOIN Handles
JOIN Zookeeper ON Handles.ZOOKEEPID = Zookeeper.ZID
ON Animal.AID = Handles.ANIMALID 
group by Zookeeper.Zname;


SELECT Handles.Assigned, Zookeeper.ZName, Animal.AName
FROM Animal
INNER JOIN Handles ON AID = Handles.ANIMALID
JOIN Zookeeper ON Handles.ZOOKEEPID = Zookeeper.ZID
ORDER BY Handles.Assigned ASC;

SELECT Animal.AName, Zookeeper.ZNAME
FROM Animal
INNER JOIN Handles ON Animal.AID = Handles.ANIMALID
JOIN Zookeeper ON Handles.ZOOKEEPID = Zookeeper.ZID; 

SELECT DISTINCT Handles.ANIMALID, Animal.ANAME 
FROM Animal
FULL OUTER JOIN Handles ON AID = Handles.ANIMALID;

/* ***Select the Animals that do not have a handler ** */
SELECT Animal.AName, AID FROM ANIMAL
WHERE NOT EXISTS 
      (SELECT ANIMALID 
       FROM HANDLES
       WHERE Animal.AID = Handles.ANIMALID);
            
  /* List all combination of animals where the difference between feeding time requirement is within
0.25 hours (e.g., Grizzly bear, 3, Bengal tiger, 2.75). Hint: this will require a self-join. Avoid
listing identical pairs such as (Grizzly bear, 3, Grizzly bear, 3) */  


select AName, AName_1, timediff from 

(select t1.AName as name1, t2.AName as name2, t1.timetofeed, t2.timetofeed, abs(t1.timetofeed - t2.timetofeed) as timediff
from animal t1
cross join animal  t2 ) 

where timediff = 0.25;  



SELECT * FROM ZOOKEEPER;
SELECT * FROM ANIMAL;
SELECT * FROM HANDLES;
