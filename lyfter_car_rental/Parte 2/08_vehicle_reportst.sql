SET search_path TO lyfter_car_rental;

SELECT *
FROM vehicles
WHERE vehicle_status= 'rented';

--testing--
SELECT * FROM lyfter_car_rental.users;
SELECT * FROM lyfter_car_rental.vehicles;
SELECT * FROM lyfter_car_rental.rentals;

SELECT *
FROM lyfter_car_rental.users
ORDER BY user_id DESC;

SELECT *
FROM lyfter_car_rental.vehicles
ORDER BY vehicle_id DESC;