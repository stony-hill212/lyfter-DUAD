-- SQLite
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    stock_available INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

ALTER TABLE products
ADD COLUMN category_id INTEGER;

INSERT INTO categories (name, description) VALUES
('Electronics', 'Devices and gadgets'),
('Clothing', 'Martial arts apparel and wearables'),
('Food', 'High protein content groceries and consumables');

UPDATE products SET category_id = 1 WHERE id = 1;
UPDATE products SET category_id = 2 WHERE id = 2;
UPDATE products SET category_id = 3 WHERE id = 3;

SELECT id, product_name, price, category_id, stock_available
FROM products;

INSERT INTO products (product_name, price, stock_available) VALUES
('iPhone 16', 900000, 5),
('RCA TV', 450000, 8),
('Shin guards', 60000, 20),
('Apple watch', 250000, 3),
('Meet snax', 1000, 50),
('MSI laptop', 1200000, 2),
('Gaming chair', 85000, 15),
('Apple airPods', 150000, 7),
('Venum T-shirt', 45000, 30),
('Protein shaker', 7000, 9);

SELECT * FROM products;

SELECT * FROM products
WHERE price > 50000;

SELECT * FROM products
WHERE product_name LIKE '%apple%';

SELECT * FROM products
ORDER BY price DESC
LIMIT 5;

UPDATE products
SET stock_available = 0
WHERE price <= 0;

UPDATE products
SET price = price + 100
WHERE stock_available < 10;

SELECT * FROM products
ORDER BY id ASC
LIMIT 10;

