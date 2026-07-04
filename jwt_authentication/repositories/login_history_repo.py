from extensions import db
from models.login_history import LoginHistory
from models.user import User

class LoginHistoryRepository:
    @staticmethod
    def create(history):
        db.session.add(history)
        db.session.commit()
        return history
    
    @staticmethod
    def get_all(user_id):
        return LoginHistory.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_all_info():
        return LoginHistory.query.all()
