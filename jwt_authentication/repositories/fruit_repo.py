from models.fruit import Fruit
from extensions import db

class FruitRepository:
    @staticmethod
    def create(fruit):
        db.session.add(fruit)
        db.session.commit()
        return fruit
    
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