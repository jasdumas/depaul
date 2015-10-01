/*
Write SQL INSERT statements to populate your database with the following data
(NOTE: remember that strings would need to use single quotes, e.g., 'Asimov')

(King, Stephen, 2, September 9 1947)
(Asimov, Isaac, 4, January 2 1920)
(Verne, Jules, 7, February 8 1828)
(Rowling, Joanne, 37, July 31 1965)

(Bloomsbury Publishing, 17, London Borough of Camden)
(Arthur A. Levine Books, 18, New York City)

(1111-111, Databases from outer space, 17)
(2222-222, Dark SQL, 17)
(3333-333, The night of the living databases, 18)

(2, 1111-111, 1)   -- Author_ID, ISBN, Author rank??
(4, 1111-111, 2)
(4, 2222-222, 2)
(7, 2222-222, 1)
(37, 3333-333, 1)
(2, 3333-333, 2)

*/

INSERT INTO Authors(
  Author_ID, Author_Lastname, Author_Firstname, Author_birthday
) VALUES ('2','King', 'Stephen', '09-SEP-1947');
INSERT INTO Authors(
  Author_ID, Author_Lastname, Author_Firstname, Author_birthday
) VALUES ('4', 'Asimov', 'Isaac', '02-JAN-1920');
INSERT INTO Authors(
  Author_ID, Author_Lastname, Author_Firstname, Author_birthday
) VALUES ('7', 'Verne', 'Jules', '08-FEB-1828');
INSERT INTO Authors(
  Author_ID, Author_Lastname, Author_Firstname, Author_birthday
) VALUES ('37', 'Rowling', 'Joanne', '31-JUL-1965');

INSERT INTO Publisher(
  Publisher_ID, Publisher_Name, Publisher_address
) VALUES ('17', 'Bloomsbury Publishing', 'London Borough of Camden');
INSERT INTO Publisher(
  Publisher_ID, Publisher_Name, Publisher_address
) VALUES ('18', 'Arthur A. Levine Books', 'New York City');

INSERT INTO Book(
  ISBN, title, Publisher_Name
) VALUES ('1111-111','Databases from outer space', '17');
INSERT INTO Book(
  ISBN, title, Publisher_Name
) VALUES ('2222-222', 'Dark SQL', '17');
INSERT INTO Book(
  ISBN, title, Publisher_Name
) VALUES ('3333-333', 'The night of the living databases', '18');

INSERT INTO BookComplete(
  Author_ID, ISBN, Author_rank
) VALUES ('2', '1111-111', '1');
INSERT INTO BookComplete(
  Author_ID, ISBN, Author_rank
) VALUES ('4', '1111-111', '2');
INSERT INTO BookComplete(
  Author_ID, ISBN, Author_rank
) VALUES ('4', '2222-222', '2');
INSERT INTO BookComplete(
  Author_ID, ISBN, Author_rank
) VALUES ('7', '2222-222', '1');
INSERT INTO BookComplete(
  Author_ID, ISBN, Author_rank
) VALUES ('37', '3333-333', '1');
INSERT INTO BookComplete(
  Author_ID, ISBN, Author_rank
) VALUES ('2', '3333-333', '2');
