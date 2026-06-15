SELECT * FROM users;
SELECT * FROM contacts;
SELECT * FROM invoices;
SELECT * FROM fruits;

UPDATE contacts;

DELETE FROM users;
DELETE FROM invoices;
DELETE FROM invoice_details;

--don't use--
DROP TABLE users CASCADE;


UPDATE users
SET role= 'ADMIN'
WHERE username= 'wolfie';

SELECT id, username, role
FROM users;

SELECT * FROM invoices;
SELECT * FROM invoice_details;
