--Copyright (c) 2014 Pearson Education, Inc.
-- Juki?, Vrbsky, Nestorov – Database Systems 


CREATE TABLE vendor
( 	vendorid 	CHAR(2) 		NOT NULL,
	vendorname 	VARCHAR(25) 	NOT NULL,
	PRIMARY KEY (vendorid) );
CREATE TABLE category
( 	categoryid 	CHAR(2) 		NOT NULL,
	categoryname 	VARCHAR(25) 	NOT NULL,
	PRIMARY KEY (categoryid) );

CREATE TABLE product
( 	productid 	CHAR(3) 		NOT NULL,
	productname 	VARCHAR(25) 	NOT NULL,
	productprice 	NUMERIC(7,2)	NOT NULL,
	vendorid 	CHAR(2) 		NOT NULL,
	categoryid 	CHAR(2) 		NOT NULL,
	PRIMARY KEY (productid),
	FOREIGN KEY (vendorid) REFERENCES vendor(vendorid),
	FOREIGN KEY (categoryid) REFERENCES category(categoryid) );

CREATE TABLE region
( 	regionid 	CHAR(1) 		NOT NULL,
	regionname 	VARCHAR(25) 	NOT NULL,
	PRIMARY KEY (regionid) );
  
CREATE TABLE store
( 	storeid 		VARCHAR(3) 	NOT NULL,
	storezip 	CHAR(5) 		NOT NULL,
	regionid 	CHAR(1) 		NOT NULL,
	PRIMARY KEY (storeid),
	FOREIGN KEY (regionid) REFERENCES region(regionid) );

CREATE TABLE customer
( 	customerid 	CHAR(7) 		NOT NULL,
	customername 	VARCHAR(15) 	NOT NULL,
	customerzip 	CHAR(5) 		NOT NULL,
	PRIMARY KEY (customerid) );

CREATE TABLE salestransaction
( 	tid 		VARCHAR(8) 	NOT NULL,
	customerid 	CHAR(7) 		NOT NULL,
	storeid 		VARCHAR(3) 	NOT NULL,
	tdate 		DATE 		NOT NULL,
	PRIMARY KEY (tid),
	FOREIGN KEY (customerid) REFERENCES customer(customerid),
	FOREIGN KEY (storeid) REFERENCES store(storeid) );

CREATE TABLE soldvia
( 	productid 	CHAR(3) 		NOT NULL,
	tid 		VARCHAR(8) 	NOT NULL,
	noofitems 	INT 		NOT NULL,
	PRIMARY KEY (productid, tid),
	FOREIGN KEY (productid) REFERENCES product(productid),
	FOREIGN KEY (tid) REFERENCES salestransaction(tid) );
  
-- populate the tables

INSERT INTO vendor VALUES ('PG','Pacifica Gear');
INSERT INTO vendor VALUES ('MK','Mountain King');

INSERT INTO category VALUES ('CP','Camping');
INSERT INTO category VALUES ('FW','Footwear');

INSERT INTO product VALUES ('1X1','Zzz Bag',100,'PG','CP');
INSERT INTO product VALUES ('2X2','Easy Boot',70,'MK','FW');
INSERT INTO product VALUES ('3X3','Cosy Sock',15,'MK','FW');
INSERT INTO product VALUES ('4X4','Dura Boot',90,'PG','FW');
INSERT INTO product VALUES ('5X5','Tiny Tent',150,'MK','CP');
INSERT INTO product VALUES ('6X6','Biggy Tent',250,'MK','CP');

INSERT INTO region VALUES ('C','Chicagoland');
INSERT INTO region VALUES ('T','Tristate');

INSERT INTO store VALUES ('S1','60600','C');
INSERT INTO store VALUES ('S2','60605','C');
INSERT INTO store VALUES ('S3','35400','T');

INSERT INTO customer VALUES ('1-2-333','Tina','60137');
INSERT INTO customer VALUES ('2-3-444','Tony','60611');
INSERT INTO customer VALUES ('3-4-555','Pam','35401');

INSERT INTO salestransaction VALUES ('T111','1-2-333','S1','01/Jan/2013');
INSERT INTO salestransaction VALUES ('T222','2-3-444','S2','01/Jan/2013');
INSERT INTO salestransaction VALUES ('T333','1-2-333','S3','02/Jan/2013');
INSERT INTO salestransaction VALUES ('T444','3-4-555','S3','02/Jan/2013');
INSERT INTO salestransaction VALUES ('T555','2-3-444','S3','02/Jan/2013');

INSERT INTO soldvia VALUES ('1X1','T111',1);
INSERT INTO soldvia VALUES ('2X2','T222',1);
INSERT INTO soldvia VALUES ('3X3','T333',5);
INSERT INTO soldvia VALUES ('1X1','T333',1);
INSERT INTO soldvia VALUES ('4X4','T444',1);
INSERT INTO soldvia VALUES ('2X2','T444',2);
INSERT INTO soldvia VALUES ('4X4','T555',4);
INSERT INTO soldvia VALUES ('5X5','T555',2);
INSERT INTO soldvia VALUES ('6X6','T555',1);

-- queries

--q1
SELECT 	productid, productname, productprice, vendorid, categoryid 	
FROM 		product;
--q1a
SELECT 	*	
FROM 		product;
--q3
SELECT 	productid, productprice 
FROM 		product;

/*
SELECT <columns, expressions>
FROM <tables>
WHERE <row selection condition>
GROUP BY <grouping columns>
HAVING <group selection condition>
ORDER BY <sorting columns, expressions>

WHERE 
= 	Equal to
<	Less than
> 	Greater than
<=	Less than or equal to
>= 	Greater than or equal to
!= 	Not equal to
<> 	Not equal to (alternative notation)
*/

--Retrieve the product id, product name, vendor id, and product 		price for each product whose price is above $100
--q 4: 	
SELECT 	productid, productname, vendorid, 	productprice		
FROM 		product 	WHERE 		productprice > 100;

--Query 16 text: 	For each vendor, retrieve the vendor id, number of products 		supplied by the vendor, and average price of the products 		supplied by the vendor
--Query 16 :
SELECT 	vendorid, COUNT(*), AVG(productprice)		
FROM 		product		GROUP BY 	vendorid;

-- show Query 16 illustration

-- remove group by
SELECT 	vendorid, COUNT(*), AVG(productprice)		
FROM 		product	;

--Query 19 text: 	Consider the groups of products where each group contains the 		products that are from the same category supplied by the same 		vendor.  For each such group, retrieve the vendor id, product 		category id, number of products in the group, and average price of		the products in the group.

--Query 19 : 
SELECT 	vendorid, categoryid, COUNT(*),		AVG(productprice)		
FROM 		product 
GROUP BY 	vendorid, categoryid;





