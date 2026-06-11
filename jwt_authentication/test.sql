SELECT * FROM users;

DROP TABLE users CASCADE;


UPDATE users
SET role= 'ADMIN'
WHERE username= 'asstastic';

SELECT id, username, role
FROM users;

SELECT * FROM invoices;
SELECT * FROM invoice_details;