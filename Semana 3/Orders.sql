-- SQLite
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGERS PRIMARY KEY,
    CustomerName TEXT,
    CustomerPhone TEXT,
    Address TEXT
);

CREATE TABLE IF NOT EXISTS Orders (
    OrderID TEXT PRIMARY KEY,
    CustomerID INTEGER,
    DeliveryTime TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

DROP TABLE IF EXISTS Items;

CREATE TABLE IF NOT EXISTS Items (
    ItemID INTEGER PRIMARY KEY,
    ItemName TEXT UNIQUE,
    Price REAL
);

DROP TABLE IF EXISTS OrderDetails;

CREATE TABLE IF NOT EXISTS OrderDetails (
    OrderID TEXT,
    ItemID INTEGER,
    Quantity INTEGER,
    SpecialRequest TEXT,
    PRIMARY KEY (OrderID, ItemID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemsID)
);

INSERT INTO Customers VALUES (1, 'Alice', '123-456-7890', '123 Derry St');
INSERT INTO Customers VALUES (2, 'Bobby', '987-654-3210', '456 Elm St');
INSERT INTO Customers VALUES (3, 'Claire', '555-123-4567', '789 Oak St');

INSERT INTO Orders VALUES ('001', 1, '6:00 PM');
INSERT INTO Orders VALUES ('002', 2, '7:30 PM');
INSERT INTO Orders VALUES ('003', 3, '12:00 PM');
INSERT INTO Orders VALUES ('004', 3, '5:00 PM');

INSERT INTO Items VALUES (101, 'Cheeseburger', 8);
INSERT INTO Items VALUES (102, 'Fries', 3);
INSERT INTO Items VALUES (103, 'Pizza', 12);
INSERT INTO Items VALUES (105, 'Salad', 6);
INSERT INTO Items VALUES (106, 'Water', 1);

INSERT INTO OrderDetails VALUES ('001', 101, 2, 'No onion');
INSERT INTO OrderDetails VALUES ('001', 102, 1, 'Extra ketchup');
INSERT INTO OrderDetails VALUES ('002', 103, 1, 'Extra cheese');
INSERT INTO OrderDetails VALUES ('002', 102, 2, 'None');
INSERT INTO OrderDetails VALUES ('003', 105, 1, 'No croutons');
INSERT INTO OrderDetails VALUES ('004', 106, 1, 'None');

SELECT * FROM Customers;
SELECT * FROM Orders;
SELECT * FROM Items;
SELECT * FROM OrderDetails;
