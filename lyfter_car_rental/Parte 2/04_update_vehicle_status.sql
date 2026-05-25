SET search_path TO lyfter_car_rental;

UPDATE vehicles
SET vehicle_status= 'rented'
WHERE vehicle_id= 1;