CREATE TABLE IF NOT EXISTS Users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    stock INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Bills (
    bill_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    status VARCHAR(20) DEFAULT 'Completed', 
    bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total NUMERIC(10,2),

    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS bill_details (
    detail_id SERIAL PRIMARY KEY,
    bill_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    subtotal NUMERIC (10,2) NOT NULL,

    CONSTRAINT fk_bill
        FOREIGN KEY(bill_id)
        REFERENCES Bills(bill_id),
    
    CONSTRAINT fk_product
        FOREIGN KEY(product_id)
        REFERENCES Products(product_id)
);

INSERT INTO Users(full_name, email, phone)
VALUES
('Jimmy Conway', 'jgent@yahoo.com', '8888-1111'),
('Jon Jones', 'bones@ufc.com', '8888-3333'),
('Margaret Thatcher', 'cunt@aol.com', '8888-2222');

INSERT INTO Products(product_name, price, stock)
VALUES
('Gabagool', 7.50, 100),
('Bialy', 2.75, 50),
('Cannoli', 8.25, 80),
('Vinegar peppers', 25.00, 1);

DO $$
DECLARE
    v_bill_id INTEGER;
    v_total NUMERIC(10,2);
BEGIN
    INSERT INTO Bills(user_id, total)
    VALUES (1, 0)
    RETURNING bill_id INTO v_bill_id;

    INSERT INTO bill_details(
        bill_id,
        product_id,
        quantity,
        subtotal
    )
    VALUES (
        v_bill_id,
        1,
        2,
        15.00
    );
    UPDATE Products
    SET stock = stock - 2
    WHERE product_id = 1;

    INSERT INTO bill_details(
        bill_id,
        product_id,
        quantity,
        subtotal
    )
    VALUES (
        v_bill_id,
        2,
        1,
        2.75
    );

    UPDATE Products
    SET stock = stock - 1
    WHERE product_id = 2;

    SELECT SUM(subtotal)
    INTO v_total
    FROM bill_details
    WHERE bill_id = v_bill_id;

    UPDATE Bills
    SET total = v_total
    WHERE bill_id = v_bill_id;

END $$;

SELECT * FROM Users;
SELECT * FROM Products;
SELECT * FROM Bills;
SELECT * FROM bill_details;