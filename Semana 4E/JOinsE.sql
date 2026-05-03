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
(50, 'Miguel de Cervantes'),
(51, 'Dante Alighieri'),
(52, 'Takehiko Inoue'),
(53, 'Akira Toriyama'),
(54, 'Walt Disney');

INSERT INTO Books VALUES
(50, 'Don Quijote', 50),
(51, 'La Divina Comedia', 51),
(52, 'Vagabond 1-3', 52),
(53, 'Dragon Ball 1', 53),
(54, 'The book of the 5 Rings', NULL);

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

SELECT
    Customers.ID,
    Customers.name,
    COUNT(Rents.ID) AS total_rents
FROM Customers
INNER JOIN Rents
    ON Customers.ID = Rents.CustomerID
GROUP BY
    Customers.ID, Customers.Name
ORDER BY
    total_rents DESC
LIMIT 3;

SELECT
    Customers.Name AS customer_name,
    Books.Name AS book_name,
    Authors.Name AS author_name,
    Rents.State AS status
FROM Rents
INNER JOIN Customers
    ON Rents.CustomerID = Customers.ID
INNER JOIN Books
    ON Rents.BookID = Books.ID
LEFT JOIN Authors
    ON Books.Author = Authors.ID;