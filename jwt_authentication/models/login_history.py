from extensions import db
from datetime import datetime

class LoginHistory(db.Model):
    __tablename__="login_history"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"),nullable=True)
    timestamp=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ip_address=db.Column(db.String(50), nullable=False)
    success=db.Column(db.Boolean, nullable=False)