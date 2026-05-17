-- Connect to database
-- \c storex_db

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

SELECT * FROM Products;
SELECT * FROM Bills;
SELECT * FROM bill_details;