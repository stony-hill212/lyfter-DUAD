from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import redis

db=SQLAlchemy()

migrate=Migrate()

jwt=JWTManager()

redis_client=redis.Redis(
    host="stony_hill",
    port=XXXX,
    password="redises-stony_hill-password",
    decode_responses=True
)
