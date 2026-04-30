-- SQLite
CREATE TABLE IF NOT EXISTS Books (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Author INTEGER
);

CREATE TABLE IF NOT EXISTS Authors (
    ID INTEGER PRIMARY KEY,
    Name TEXT
);

CREATE TABLE IF NOT EXISTS Customers (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Email TEXT
);

CREATE TABLE IF NOT EXISTS Rents (
    ID INTEGER PRIMARY KEY,
    BookID INTEGER,
    CustomerID INTEGER,
    State TEXT
);

INSERT INTO Authors VALUES
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');

INSERT INTO Books VALUES
(1, 'Don Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Vagabond 1-3', 3),
(4, 'Dragon Ball 1', 4),
(5, 'The book of the 5 Rings', NULL);

SELECT Books.Name AS Book, Authors.Name AS Author
FROM Books
LEFT JOIN Authors ON Books.Author = Authors.ID;

SELECT Books.Name
FROM Books
LEFT JOIN Authors ON Books.Author = Authors.ID
WHERE Authors.ID IS NULL;

SELECT Authors.Name
FROM Authors
LEFT JOIN Books ON Authors.ID = Books.Author
WHERE Books.ID IS NULL;

SELECT DISTINCT Books.Name
FROM Books
INNER JOIN Rents ON Books.ID = Rents.BookID;

SELECT Books.Name
FROM Books
LEFT JOIN Rents ON Books.ID = Rents.BookID
WHERE Rents.ID IS NULL;

SELECT Customers.Name
FROM Customers
LEFT JOIN Rents ON Customers.ID = Rents.CustomerID
WHERE Rents.ID IS NULL;

SELECT Books.Name
FROM Books
INNER JOIN Rents ON Books.ID = Rents.BookID
WHERE Rents.State = 'Overdue';
