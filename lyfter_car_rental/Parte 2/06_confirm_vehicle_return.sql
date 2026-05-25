SET search_path TO lyfter_car_rental;

UPDATE rentals
SET rental_status= 'completed'
WHERE rental_id= 1;

UPDATE vehicles
SET vehicle_status= 'available'
WHERE vehicle_id= 1;