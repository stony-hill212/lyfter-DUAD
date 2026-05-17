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
    status VARCHAR(20) DEFAULT 'Pending', 
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
    delivered BOOLEAN DEFAULT FALSE,

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

DO $$
DECLARE
    v_user_exist INTEGER;
    v_bill_id INTEGER;
    v_total NUMERIC(10,2) := 0;

    rec RECORD;

BEGIN
    SELECT COUNT(*)
    INTO v_user_exist
    FROM Users
    WHERE user_id = 1;

    IF v_user_exist = 0 THEN
        RAISE EXCEPTION 'User does not exist';
    END IF;

    INSERT INTO Bills(user_id, total)
    VALUES (1, 0)
    RETURNING bill_id INTO v_bill_id;

    FOR rec INSERT
        SELECT
            p.product_id,
            p.price,
            p.stock,
            x.quantity
        FROM Products p
        JOIN (
            VALUES
                (1, 3),
                (2, 2)
        ) AS x(product_id, quantity)
        ON p.product_id = x.product_id
    LOOP
        IF rec.stock < rec.quantity THEN
            RAISE EXCEPTION 'Not enough stock for product %',
            rec.product_id;
        END IF;

        INSERT INTO bill_details(
            bill_id,
            product_id,
            quantity,
            subtotal
        )
        VALUES (
            v_bill_id,
            rec.product_id,
            rec.quantity,
            rec.quantity * rec.price
        );

        UPDATE Products
        SET stock = stock - rec.quantity
        WHERE product_id = rec.product_id;
        v_total :=
            v_total + (rec.quantity * rec.price);

    END LOOP;

    UPDATE Bills
    SET total = v_total
    WHERE bill_id = v_bill_id;

END $$;

DO $$
DECLARE
    v_bill_exists INTEGER;

    rec RECORD;

BEGIN
    SELECT COUNT(*)
    INTO v_bill_exists
    FROM Bills
    WHERE bill_id = 1;

    IF v_bill_exists = 0 THEN
        RAISE EXCEPTION 'Bill does not exist';
    END IF;

    FOR rec IN
        SELECT
            product_id,
            quantity
        FROM bill_details
        WHERE bill_id = 1
    LOOP
        UPDATE Products
        SET stock = stock + rec.quantity
        WHERE product_id = rec.product_id;
    
    END LOOP;

    UPDATE Bills
    SET status = 'Returned'
    WHERE bill_id = 1;

END $$;

INSERT INTO Bills(user_id, total, status)
VALUES (1, 20.00, 'Pending');

INSERT INTO bill_details(
    bill_id,
    product_id,
    quantity,
    subtotal
)
VALUES
(2, 1, 2, 5.00),
(2, 2, 3, 15.00);

DO $$
DECLARE
    v_bill_exists INTEGER;
    v_bill_status VARCHAR(20);

    rec RECORD;

BEGIN
    SELECT COUNT(*)
    INTO v_bill_exists
    FROM Bills
    WHERE bill_id = 2;

    IF v_bill_exists = 0 THEN
        RAISE EXCEPTION 'Invoice does not exist';
    END IF;

    SELECT status
    INTO v_bill_status
    FROM Bills
    WHERE bill_id = 2;

    IF v_bill_status <> 'Pending' THEN
        RAISE EXCEPTION 'Invoice is not pending';
    END IF;

    FOR rec IN
        SELECT
            product_id,
            quantity
        FROM bill_details
        WHERE bill_id = 2
        AND delivered = FALSE
    LOOP
        UPDATE Products
        SET stock = stock + rec.quantity
        WHERE product_id = rec.product_id;
    END LOOP;

    UPDATE Bills
    SET status = 'Cancelled'
    WHERE bill_id = 2;

END $$;

DO $$
DECLARE
    v_bill_id INTEGER;

    v_stock_product1 INTEGER;
    v_stock_product2 INTEGER;
    v_stock_product3 INTEGER;

    v_price_product1 NUMERIC(10,2);
    v_price_product2 NUMERIC(10,2);
    v_price_product3 NUMERIC(10,2);

    v_total NUMERIC(10,2);

    v_quantity_product1 INTEGER := 2;
    v_quantity_product2 INTEGER := 3;
    v_quantity_product3 INTEGER := 100;
BEGIN
    
    SELECT stock, price
    INTO v_stock_product1, v_price_product1
    FROM Products
    WHERE product_id = 1;

    SELECT stock, price
    INTO v_stock_product2, v_price_product2
    FROM Products
    WHERE product_id = 2;

    SELECT stock, price
    INTO v_stock_product3, v_price_product3
    FROM Products
    WHERE product_id = 4;

    IF v_stock_product1 < v_quantity_product1 THEN
        RAISE EXCEPTION 'Insufficient stock for product 1';
    END IF;

    IF v_stock_product2 < v_quantity_product2 THEN
        RAISE EXCEPTION 'Insufficient stock for product 2';
    END IF;

    IF v_stock_product3 < v_quantity_product3 THEN
        RAISE EXCEPTION 'Insufficient stock for product 3';
    END IF;

    v_total :=
        (v_quantity_product1 * v_price_product1)
        +
        (v_quantity_product2 * v_price_product2)
        +
        (v_quantity_product3 * v_price_product3);

    INSERT INTO Bills(user_id, total, status)
    VALUES (1, v_total, 'Completed')
    RETURNING bill_id INTO v_bill_id;

    INSERT INTO bill_details(
        bill_id,
        product_id,
        quantity,
        subtotal
    )
    VALUES
    (
        v_bill_id,
        1,
        v_quantity_product1,
        v_quantity_product1 * v_price_product1
    ),
    (
        v_bill_id,
        2,
        v_quantity_product2,
        v_quantity_product2 * v_price_product2
    ),
    (
        v_bill_id,
        4,
        v_quantity_product3,
        v_quantity_product3 * v_price_product3
    );

    UPDATE Products 
    SET stock = stock - v_quantity_product1
    WHERE product_id = 1;

    UPDATE Products 
    SET stock = stock - v_quantity_product2
    WHERE product_id = 2;

    UPDATE Products 
    SET stock = stock - v_quantity_product3
    WHERE product_id = 4;

END $$;

DO $$
DECLARE
    v_current_stock INTEGER;
    
BEGIN
    
    SELECT stock
    INTO v_current_stock
    FROM Products
    WHERE product_id = 4;
    IF v_current_stock <= 0 THEN
        RAISE EXCEPTION 'Product out of stock';
    END IF;

    UPDATE Products
    SET stock = stock - 1
    WHERE product_id = 4
    AND stock = v_current_stock;
    IF NOT FOUND THEN 
        RAISE EXCEPTION 'Stock changed by another transaction';
    END IF;

END $$;
