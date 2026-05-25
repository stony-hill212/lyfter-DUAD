# Lyfter Car Rental backend system

## Descripción:

Este proyecto es un sistema backend para el ejercicio de SQL en Python, para una compañía ficticia de alquiler de automóviles.

El sistema se desarrolló usando:
•	PostgreSQL
•	SQL
•	Python
•	Flask
•	Principios de REST API

El proyecto se dividió en 3 partes principales:
1.	Crear y popular la DB
2.	Pruebas básicas de la DB
3.	Creación del API

# Estructura del proyecto:

```text
lyfter_car_rental/
│
├── Parte 1/
│   ├── 01_schema.sql
│   ├── 02_users.sql
│   ├── 03_vehicles.sql
│   └── 04_rentals.sql
│
├── Parte 2/
│   ├── 01_add_user.sql
│   ├── 02_add_vehicle.sql
│   ├── 03_update_user_status.sql
│   ├── 04_update_vehicle_status.sql
│   ├── 05_create_rental.sql
│   ├── 06_confirm_vehicle_return.sql
│   ├── 07_disable_vehicle.sql
│   └── 08_vehicle_reports.sql
│
├── Parte 3/
│   ├── app.py
│   ├── db.py
│   └── requirements.txt
│
└── README.m

# Nota: Todos los endpoints solicitados fueron probados en Postman exitosamente.