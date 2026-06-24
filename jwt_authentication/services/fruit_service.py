from repositories.fruit_repo import FruitRepository
from datetime import datetime
from extensions import redis_client
import json

class FruitService:
    @staticmethod
    def create_fruit(data):
        fruit=FruitRepository.create_fruit(
            data["name"],
            data["price"],
            data["amount"],
            datetime.strptime(data["arrival_date"],"%Y-%m-%d").date()
        )
        redis_client.delete("fruits:all")
        return fruit

    @staticmethod
    def get_all_fruits():
        cache_key="fruits:all"
        cached_fruits=redis_client.get(cache_key)
        if cached_fruits:
            print("ALL FRUITS HIT THE CACHE")
            return json.loads(cached_fruits)
        print("ALL FRUITS CACHE MISS")
        fruits=FruitRepository.get_all()
        fruits_data=[fruit.to_dict() for fruit in fruits]
        redis_client.set(cache_key, json.dumps(fruits_data, default=str),ex=600)
        return fruits_data
    
    @staticmethod
    def get_fruit_by_id(fruit_id):
        cache_key=f"fruit: {fruit_id}"
        cached_fruit=redis_client.get(cache_key)
        if cached_fruit:
            print("CACHE HIT")
            return json.loads(cached_fruit)
        print("CACHE MISS")
        fruit=FruitRepository.get_by_id(fruit_id)
        if not fruit:
            return None
        fruit_data=fruit.to_dict()
        redis_client.set(cache_key, json.dumps(fruit_data, default=str),ex=600)
        return fruit_data
    
    @staticmethod
    def update_fruit(fruit_id, data):
        fruit=FruitRepository.get_by_id(fruit_id)
        if not fruit:
            return None
        fruit.name=data.get("name", fruit.name)
        fruit.price=data.get("price", fruit.price)
        fruit.amount=data.get("amount", fruit.amount)
        arrival_date=data.get("arrival_date")
        if arrival_date:
            fruit.arrival_date=datetime.strptime(arrival_date, "%Y-%m-%d").date()
        FruitRepository.update()
        redis_client.delete(f"fruit: {fruit_id}")
        redis_client.delete("fruits:all")
        return fruit
    
    @staticmethod
    def delete_fruit(fruit_id):
        fruit=FruitRepository.get_by_id(fruit_id)
        if not fruit:
            return False
        FruitRepository.delete(fruit)
        redis_client.delete(f"fruit: {fruit_id}")
        redis_client.delete("fruits:all")
        return True
