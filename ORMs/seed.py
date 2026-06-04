from faker import Faker
import random

from managers import(UserManager, AddressManager, CarManager)
fake=Faker()

user_manager=UserManager()
address_manager=AddressManager()
car_manager=CarManager()

create_user_ids=[]

for _ in range(20):
    user_id=user_manager.create_user(
        fake.name(),
        fake.email(),
    )
    create_user_ids.append(user_id)
    address_manager.create_address(
        fake.street_address(),
        user_id
    )
print(f"Users and addresses generated.")

makes=[
    "Ford",
    "Toyota",
    "Honda",
    "Chevrolet",
    "Nissan"
]
models=[
    "Mustang",
    "Corolla",
    "Civic",
    "Camaro",
    "Sentra"
]

for _ in range(30):
    make=random.choice(makes)
    model=random.choice(models)
    assign_owner=random.choice(
        [True, False]
    )
    if assign_owner:
        user_id=random.choice(create_user_ids)
    else:
        user_id=None
    car_manager.create_car(make, model, user_id)
print("Cars generated")

print(f"Generated {len(create_user_ids)} users.")