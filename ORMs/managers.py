from database import SessionLocal
from models import User, Address, Car
from sqlalchemy import func

class UserManager:
    def create_user(self, name, email):
        session=SessionLocal()
        user=User(
            name=name,
            email=email
        )
        session.add(user)
        session.commit()
        user_id=user.id
        session.close()
        return user_id

    def get_all_users(self):
        session=SessionLocal()
        all_users=session.query(User).all()
        session.close()
        return all_users

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
    
    def users_with_multiple_cars(self):
        session=SessionLocal()
        users=(
            session.query(User)
            .join(Car)
            .group_by(User.id)
            .having(func.count(Car.id)>1)
            .all()
        )
        session.close()
        return users
    
    def get_user_details(self, user_id):
        session=SessionLocal()
        user=session.get(User, user_id)
        if not user:
            session.close()
            return None
        result={
            "id":user.id,
            "name":user.name,
            "email":user.email,
            "addresses":[Address.street for address in user.addresses],
            "cars":[
                f"{car.make} {car.model}"
                for car in user.cars
            ]
        }
        session.close()
        return result

class AddressManager:
    def create_address(self, street, user_id):
        session=SessionLocal()
        address=Address(street=street, user_id=user_id)
        session.add(address)
        session.commit()
        address_id=address.id
        session.close()
        return address_id
    
    def address_with_street(self):
        session=SessionLocal()
        addresses=(
            session.query(Address)
            .filter(
                (Address.street.contains("Street")) | 
                (Address.street.contains("St"))
            )
            .all()
        )
        session.close()
        return addresses
    
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
        car_id=car.id
        session.close()
        return car_id
    
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

    def get_unassigned_cars(self):
        session=SessionLocal()
        cars=session.query(Car)\
                    .filter(Car.user_id==None)\
                    .all()
        session.close()
        return cars
