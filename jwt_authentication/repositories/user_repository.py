from models.user import User
from extensions import db

class UserRepository:
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def create_user(username, password, role="USER"):
        user=User(
            username=username,
            password=password,
            role=role
        )
        db.session.add(user)
        db.session.commit()
        return user