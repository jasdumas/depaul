/*
Part 1
Write SQL DDL to create the 3NF tables you created. Remember to declare primary
 and foreign keys as necessary in your SQL code.
*/

DROP TABLE RecordNumber;
CREATE TABLE RecordNumber(
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
 Record_Num VARCHAR(12) NOT NULL,

 CONSTRAINT Rec_pk
  PRIMARY KEY(Record_Num)
);

DROP TABLE ChauffeurCity;
CREATE TABLE ChauffeurCity(
  Chauffeur_city CHAR(15),
  Chauffeur_state CHAR(15),

  CONSTRAINT Chf_pk
    PRIMARY KEY(Chauffeur_city),

  CONSTRAINT Chf_fk
    FOREIGN KEY (Chauffeur_city)
      REFERENCES RecordNumber(Chauffeur_city)
);
