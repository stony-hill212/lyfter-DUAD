from database import engine, Base, SessionLocal
from models import User, Address, Car
from managers import UserManager, AddressManager, CarManager

Base.metadata.create_all(bind=engine)

print("Tables verified.")


#testing#
session=SessionLocal()
user=session.get(User, 1)
print(user.name)

for address in user.addresses:
    print(address.street)

for car in user.cars:
    print(car.make, car.model)

session.close()