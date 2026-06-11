from repositories.user_repository import UserRepository

class AuthService:
    @staticmethod
    def register(username, password):
        existing_user=(UserRepository.get_by_username(username))
        if existing_user:
            return None
        return UserRepository.create_user(
            username,
            password
        )
    @staticmethod
    def login(username, password):
        user=UserRepository.get_by_username(username)
        if user is None:
            return None
        if user.password!=password:
            return None
        return user
    
    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_by_id(user_id)