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

SELECT * FROM Products;
SELECT * FROM Bills;
SELECT * FROM bill_details;