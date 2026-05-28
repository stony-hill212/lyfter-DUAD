SET search_path TO lyfter_car_rental;

UPDATE vehicles
SET vehicle_status= 'disabled'
WHERE vehicle_id= 2;