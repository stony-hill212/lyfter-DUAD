SET search_path TO lyfter_car_rental;

CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id SERIAL PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    vehicle_condition VARCHAR(30) NOT NULL
);

INSERT INTO vehicles (
    make,
    model,
    year,
    vehicle_condition
)
VALUES
('Toyota', 'Corolla', 2020, 'Excellent'),
('Honda', 'Civic', 2019, 'Good'),
('Ford', 'Mustang', 2021, 'Excellent'),
('Chevrolet', 'Malibu', 2018, 'Fair'),
('Nissan', 'Sentra', 2022, 'Excellent'),
('BMW', 'X5', 2020, 'Good'),
('Audi', 'A4', 2021, 'Excellent'),
('Hyundai', 'Elantra', 2019, 'Good'),
('Kia', 'Sportage', 2023, 'Excellent'),
('Tesla', 'Model 3', 2022, 'Excellent');

ALTER TABLE lyfter_car_rental.vehicles
ADD COLUMN vehicle_status VARCHAR(20) NOT NULL DEFAULT 'available';