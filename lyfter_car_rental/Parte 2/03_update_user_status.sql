SET search_path TO lyfter_car_rental;

UPDATE users
SET account_status= 'inactive'
WHERE user_id= 1;