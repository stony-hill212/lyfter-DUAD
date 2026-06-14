from models.fruit import Fruit
from extensions import db

class FruitRepository:
    @staticmethod
    def create(fruit):
        db.session.add(fruit)
        db.session.commit()
        return fruit
    
    @staticmethod
    def create_fruit(name, price, amount, arrival_date):
        fruit=Fruit(
            name=name,
            price=price,
            amount=amount,
            arrival_date=arrival_date
        )
        return FruitRepository.create(fruit)
    
    @staticmethod
    def get_all():
        return Fruit.query.all()
    
    @staticmethod
    def get_by_id(fruit_id):
        return Fruit.query.get(fruit_id)
    
    @staticmethod
    def delete(fruit):
        db.session.delete(fruit)
        db.session.commit()
    
    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()
