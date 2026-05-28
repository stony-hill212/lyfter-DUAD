SET search_path TO lyfter_car_rental;

CREATE TABLE IF NOT EXISTS rentals (
    rental_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    vehicle_id INTEGER NOT NULL,
    rental_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rental_status VARCHAR(30) NOT NULL DEFAULT 'active',
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES users(user_id),
    CONSTRAINT fk_vehicle
        FOREIGN KEY(vehicle_id)
        REFERENCES vehicles(vehicle_id)
);

INSERT INTO rentals (user_id, vehicle_id, rental_status)
VALUES (1, 1, 'active');

SELECT * FROM lyfter_car_rental.users;
SELECT * FROM lyfter_car_rental.vehicles;
SELECT * FROM lyfter_car_rental.rentals;

SELECT schema_name
FROM information_schema.schemata
WHERE schema_name= 'lyfter_car_rental';