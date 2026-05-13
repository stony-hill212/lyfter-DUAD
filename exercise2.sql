-- Connect to database
-- \c storex_db

DO $$
DECLARE
    v_user_exist INTEGER;
    v_bill_id INTEGER;

    v_stock_product1 INTEGER;
    v_stock_product2 INTEGER;

    v_price_product1 NUMERIC(10,2);
    v_price_product2 NUMERIC(10,2);

    v_total NUMERIC(10,2);

    v_quantity_product1 INTEGER := 3;
    v_quantity_product2 INTEGER := 2;

BEGIN
    SELECT COUNT(*)
    INTO v_user_exist
    FROM Users
    WHERE user_id = 1;

    IF v_user_exist = 0 THEN
        RAISE EXCEPTION 'User does not exist';
    END IF;

    SELECT stock, price
    INTO v_stock_product1, v_price_product1
    FROM Products
    WHERE product_id = 1;

    SELECT stock, price
    INTO v_stock_product2, v_price_product2
    FROM Products
    WHERE product_id = 2;

    IF v_stock_product1 < v_quantity_product1 THEN
        RAISE EXCEPTION 'Not enough items in stock for product 1';
    END IF;

    IF v_stock_product2 < v_quantity_product2 THEN
        RAISE EXCEPTION 'Not enough items in stock for product 2';
    END IF;

    v_total :=
        (v_quantity_product1 * v_price_product1)+(v_quantity_product2*v_price_product2);

    INSERT INTO Bills(user_id, total)
    VALUES (1, v_total)
    RETURNING bill_id INTO v_bill_id;

    INSERT INTO bill_details(bill_id, product_id, quantity, subtotal)
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
    );

    UPDATE Products
    SET stock = stock - v_quantity_product1
    WHERE product_id = 1;

    UPDATE Products
    SET stock = stock - v_quantity_product2
    WHERE product_id = 2;
END $$;

SELECT * FROM Products;
SELECT * FROM Bills;
SELECT * FROM bill_details;