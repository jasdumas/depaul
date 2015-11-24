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


/*Query 28 text: 	For each product whose product price is below the average price
of all products, retrieve the product id, product name, and product		price*/

SELECT	productid, productname, productprice	
FROM 	product		WHERE 	productprice < ( SELECT AVG(productprice) FROM product);

/*Query 29 text:  For each product that has more than three items sold within 
all sales transactions, retrieve the product id, product name, and product price.*/
SELECT productid FROM soldvia
      GROUP BY productid 	HAVING SUM(noofitems) > 3;

-- IN
SELECT productid, productname, productprice
FROM product
WHERE productid IN 
      (SELECT productid FROM soldvia		
      GROUP BY productid 	HAVING SUM(noofitems) > 3);

--find information about every product that has been sold multiple times
SELECT 	productid, productname, productprice
FROM 		product
WHERE 		productid IN
(SELECT productid FROM soldvia
GROUP BY productid	 HAVING COUNT(*) > 1);

