from database import SessionLocal
from models import User, Address, Car

class UserManager:
    def create_user(self, name, email):
        session=SessionLocal()
        user=User(
            name=name,
            email=email
        )
        session.add(user)
        session.commit()
        return user

    def get_all_users(self):
        session=SessionLocal()
        user=session.query(User).all()
        session.close()
        return user

    def delete_user(self, user_id):
        session=SessionLocal()
        user=session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
        session.close()

    def update_user(self, user_id, name, email):
        session=SessionLocal()
        user=session.get(User, user_id)
        if user:
            user.name=name
            user.email=email
            session.commit()
        session.close()
        return user

class AddressManager:
    def create_address(self, street, user_id):
        session=SessionLocal()
        address=Address(street=street, user_id=user_id)
        session.add(address)
        session.commit()
        session.close()
        return address
    
    def get_all_addresses(self):
        session=SessionLocal()
        addresses=session.query(Address).all()
        session.close()
        return addresses
    
    def update_address(self, address_id, street):
        session=SessionLocal()
        address=session.get(Address, address_id)
        if address:
            address.street=street
            session.commit()
        session.close()
    
    def delete_address(self, address_id):
        session=SessionLocal()
        address=session.get(Address, address_id)
        if address:
            session.delete(address)
            session.commit()
        session.close()
    
class CarManager:
    def create_car(self, make, model, user_id=None):
        session=SessionLocal()
        car=Car(
            make=make,
            model=model,
            user_id=user_id
        )
        session.add(car)
        session.commit()
        session.close()
        return car
    
    def get_all_cars(self):
        session=SessionLocal()
        cars=session.query(Car).all()
        session.close()
        return cars
    
    def update_car(self, car_id, make, model):
        session=SessionLocal()
        car=session.get(Car, car_id)
        if car:
            car.make=make
            car.model=model
            session.commit()
        session.close()
    
    def delete_car(self, car_id):
        session=SessionLocal()
        car=session.get(Car, car_id)
        if car:
            session.delete(car)
            session.commit()
        session.close()
    
    def assign_car_to_user(self, car_id, user_id):
        session=SessionLocal()
        car=session.get(Car, car_id)
        if car:
            car.user_id=user_id
            session.commit()
        session.close()