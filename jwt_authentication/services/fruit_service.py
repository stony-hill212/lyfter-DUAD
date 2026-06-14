from repositories.fruit_repo import FruitRepository

class FruitService:
    @staticmethod
    def get_all_fruits():
        return FruitRepository.get_all()
    
    @staticmethod
    def get_fruit_by_id(fruit_id):
        return FruitRepository.get_by_id(fruit_id)
    
    @staticmethod
    def update_fruit(fruit_id, data):
        fruit=FruitRepository.get_by_id(fruit_id)
        if not fruit:
            return None
        fruit.name=data.get("name", fruit.name)
        fruit.price=data.get("price", fruit.price)
        fruit.amount=data.get("amount", fruit.amount)
        fruit.arrival_date=data.get("arrival_date", fruit.arrival_date)
        FruitRepository.update()
        return fruit
    
    @staticmethod
    def delete_fruit(fruit_id):
        fruit=FruitRepository.get_by_id(fruit_id)
        if not fruit:
            return False
        FruitRepository.delete(fruit)
        return True
