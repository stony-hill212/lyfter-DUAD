from models.login_history import LoginHistory
from repositories.login_history_repo import LoginHistoryRepository

class LoginHistoryService:
    @staticmethod
    def log_attempt(user_id, ip_address, success):
        history=LoginHistory(
            user_id=user_id,
            ip_address=ip_address,
            success=success
        )
        return LoginHistoryRepository.create(history)
    @staticmethod
    def get_all():
        return LoginHistoryRepository.get_all()