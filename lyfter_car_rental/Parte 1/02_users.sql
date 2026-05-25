SET search_path TO lyfter_car_rental;

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    account_status VARCHAR(20) NOT NULL DEFAULT 'active',
    DOB DATE NOT NULL
);

ALTER TABLE lyfter_car_rental.users
ADD COLUMN overdue BOOLEAN DEFAULT FALSE;

INSERT INTO users (
    full_name,
    email,
    username,
    password,
    account_status,
    DOB
)
SELECT
    'User' || num,
    'user' || num || '@mail.com',
    'user' || num,
    'password' || num,
    CASE
        WHEN num % 2 = 0 THEN 'active'
        ELSE 'inactive'
    END,
    DATE '1998-01-01' + (num*30)
FROM generate_series(1, 50) AS num
ON CONFLICT (email) DO NOTHING;