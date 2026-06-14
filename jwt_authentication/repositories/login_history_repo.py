from extensions import db
from models.login_history import LoginHistory

class LoginHistoryRepository:
    @staticmethod
    def create(history):
        db.session.add(history)
        db.session.commit()
        return history
    
    @staticmethod
    def get_all():
        return LoginHistory.query.all()