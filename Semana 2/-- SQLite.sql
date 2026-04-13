-- SQLite
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Users (full_name, email)
VALUES ('Sandor Clegane', 'hound@hisown.com');

SELECT * FROM Users;

CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL CHECK (price >= 0),
    stock INTEGER NOT NULL CHECK (stock >= 0)
);

INSERT INTO Products (name, price, stock)
VALUES ('Laptop', 700000, 8);

SELECT * FROM Products;

CREATE TABLE IF NOT EXISTS Payment_methods (
    method_id INTEGER PRIMARY KEY AUTOINCREMENT,
    method_type TEXT NOT NULL,
    bank_name TEXT
);

INSERT INTO Payment_methods (method_type, bank_name)
VALUES ('Card', 'Wells Fargo');

SELECT * FROM Payment_methods;

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Invoices (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    method_id INTEGER NOT NULL,
    total_amount REAL NOT NULL CHECK (total_amount >= 0),
    invoice_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (method_id) REFERENCES Payment_methods(method_id)
);

INSERT INTO Invoices (user_id, method_id, total_amount)
VALUES (1, 1, 150000);

SELECT * FROM Invoices;

CREATE TABLE IF NOT EXISTS Products_per_invoice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    total_amount REAL NOT NULL CHECK (total_amount >= 0),

    FOREIGN KEY (invoice_id) REFERENCES Invoices(invoice_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Products_per_invoice (invoice_id, product_id, quantity, total_amount)
VALUES (1, 1, 2, 150000);

SELECT * FROM Products_per_invoice;

CREATE TABLE IF NOT EXISTS Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    comment TEXT,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

INSERT INTO Reviews (product_id, user_id, comment, rating)
VALUES (1, 1, 'Great service', 5);

SELECT * FROM Reviews;

CREATE TABLE IF NOT EXISTS Shopping_cart (
    cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Shopping_cart_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),

    FOREIGN KEY (cart_id) REFERENCES Shopping_cart(cart_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Shopping_cart (buyer_email)
VALUES ('hound@hisown.com');

INSERT INTO Shopping_cart_items (cart_id, product_id, quantity)
VALUES (1, 1, 3);

SELECT * FROM Shopping_cart_items;

ALTER TABLE Invoices
ADD COLUMN buyer_phone TEXT;

ALTER TABLE Invoices
ADD COLUMN employee_code TEXT;

PRAGMA table_info(Invoices);

SELECT * FROM Products;

SELECT * 
FROM Products
WHERE price > 50000;

SELECT *
FROM Products_per_invoice
WHERE product_id = 1;

SELECT
    product_id,
    SUM(total_amount) AS total_income
FROM Products_per_invoice ppi
JOIN Products p ON ppi.product_id = p.product_id
GROUP BY p.name;

SELECT * 
    u.full_name,
    i.*
FROM Invoices i 
JOIN u.user_id = 1;

SELECT * 
FROM Invoices
ORDER BY total_amount DESC;

SELECT DISTINCT invoice_id
FROM Invoices;





