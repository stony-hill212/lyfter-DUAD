from database import engine, Base, SessionLocal
from models import User, Address, Car
from managers import UserManager, AddressManager, CarManager

Base.metadata.create_all(bind=engine)

print("Tables verified.")


#testing#
session=SessionLocal()

car_manager=CarManager()
user_manager=UserManager()
address_manager=AddressManager()

user_manager.create_user("Robert Paulsen", "bobby@fightclub.com")
print("User created")

users=user_manager.get_all_users()
for user in users:
    print(user.id, user.name, user.email)

cars=car_manager.get_all_cars()
for car in cars:
    print(car.id, car.make, car.model)

user=session.get(User, 2)
print(user.name)

for address in user.addresses:
    print(address.street)

for car in user.cars:
    print(car.make, car.model)

car_manager.create_car("Shelby", "Cobra")
unassigned_cars=car_manager.get_unassigned_cars()
for car in unassigned_cars:
    print(
        car.id,
        car.make,
        car.model,
        car.user_id
    )

car_manager.create_car("Maserati", "Granturismo")
car_manager.assign_car_to_user(3, 3)

users=user_manager.users_with_multiple_cars()
for user in users:
    print(user.id, user.name)

address_manager.create_address("101 Elm St", 1)
address_manager.create_address("15 hells kitchen ave", 1)
address_manager.create_address("777 newark Street", 1)

addresses=address_manager.address_with_street()
for address in addresses:
    print(address.id, address.street)

print("-----Unassigned cars----")
for car in car_manager.get_unassigned_cars():
    print(car.id, car.make, car.model)

print("---users with multiple cars:----")
for user in user_manager.users_with_multiple_cars():
    print(user.id, user.name)

print("---addresses with street----")
for address in address_manager.address_with_street():
    print(address.id, address.street)

details=user_manager.get_user_details(3)
print(details)

session.close()
