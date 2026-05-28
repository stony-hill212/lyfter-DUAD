import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from faker import Faker

from shared_db.main_db import get_connection

fake=Faker()

CAR_BRANDS=[
    "Toyota",
    "Honda",
    "Ford",
    "BMW",
    "Audi",
    "Nissan",
    "Chevrolet",
    "Hyundai"
]
CAR_MODELS=[
    "Corolla",
    "Civic",
    "Mustang",
    "X5",
    "A4",
    "Sentra",
    "Camaro",
    "Elentra"
]

statuses= ["active", "suspended", "inactive"]
conditions=["Excellent", "Fair", "Good", "Dope", "Decent"]

def create_users(cursor):
    users=[]
    for _ in range(200):
        users.append((
            fake.name(),
            fake.unique.email(),
            fake.unique.user_name(),
            fake.password(),
            random.choice(statuses),
            fake.date_of_birth(minimum_age=18, maximum_age=80)
        ))
    cursor.executemany("""
        INSERT INTO lyfter_car_rental.users (full_name, email, username, password, account_status, DOB)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, users)
    print("200 users inserted")

def create_vehicles(cursor):
    vehicles=[]
    for _ in range(100):
        vehicles.append((
            random.choice(CAR_BRANDS),
            random.choice(CAR_MODELS),
            random.randint(2005, 2026),
            random.choice(conditions),
            random.choice(statuses)
        ))
    cursor.executemany("""
        INSERT INTO lyfter_car_rental.vehicles (make, model, year, vehicle_condition, vehicle_status)
        VALUES (%s, %s, %s, %s, %s)
    """, vehicles)
    print("100 vehicles inserted")

def create_rentals(cursor):
    rentals=[]
    rental_count=random.randint(50, 100)
    for _ in range(rental_count):
        rentals.append((
            random.randint(1, 200),
            random.randint(1, 100),
            fake.date_this_year()
        ))
    cursor.executemany("""
        INSERT INTO lyfter_car_rental.rentals (
            user_id,
            vehicle_id,
            rental_date             
        )
        VALUES (%s, %s, %s)
    """, rentals)
    print(f"{rental_count} rentals inserted")

def main():
    conn=get_connection()
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT current_database();")
        print(cursor.fetchone())
        cursor.execute("""
            TRUNCATE lyfter_car_rental.rentals, lyfter_car_rental.users, lyfter_car_rental.vehicles
            RESTART IDENTITY CASCADE
        """)
        create_users(cursor)
        create_vehicles(cursor)
        create_rentals(cursor)
        conn.commit()
        print("Database seeded successfully")
    except Exception as error:
        conn.rollback()
        print(f"Error: {error}")
    finally:
        cursor.close()
        conn.close()


if __name__=="__main__":
    main()