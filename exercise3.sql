--Connect to database
-- \c storex_db

DO $$
DECLARE
    v_bill_exists INTEGER;

    v_quantity_product1 INTEGER;
    v_quantity_product2 INTEGER;

BEGIN
    SELECT COUNT(*)
    INTO v_bill_exists
    FROM Bills
    WHERE bill_id = 1;
    IF v_bill_exists = 0 THEN
        RAISE EXCEPTION 'Bill does not exist';
    END IF;

    SELECT quantity
    INTO v_quantity_product1
    FROM bill_details
    WHERE bill_id = 1
    AND product_id = 1;

    SELECT quantity
    INTO v_quantity_product2
    FROM bill_details
    WHERE bill_id = 1
    AND product_id = 2;

    UPDATE Products
    SET stock = stock + v_quantity_product1
    WHERE product_id = 1;

    UPDATE Products
    SET stock = stock + v_quantity_product2
    WHERE product_id = 2;

    UPDATE Bills
    SET status = 'Returned'
    WHERE bill_id = 1;

END $$;

SELECT * FROM Products;
SELECT * FROM Bills;
SELECT * FROM bill_details;