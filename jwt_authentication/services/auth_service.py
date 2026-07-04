from repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash

class AuthService:
    @staticmethod
    def register(username, password):
        existing_user=(UserRepository.get_by_username(username))
        if existing_user:
            return None
        hashed_password=generate_password_hash(password)
        return UserRepository.create_user(
            username,
            hashed_password
        )
    @staticmethod
    def login(username, password):
        user=UserRepository.get_by_username(username)
        if user is None:
            return None
        if not check_password_hash(user.password, password):
            return None
        return user
    
    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_by_id(user_id)
