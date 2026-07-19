from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR=Path(__file__).resolve().parent

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    with open(BASE_DIR/"keys/private.pem","r")as file:
        PRIVATE_KEY=file.read()
    with open(BASE_DIR/"keys/public.pem","r")as file:
        PUBLIC_KEY=file.read()

    JWT_ALGORITHM="RS256"
    JWT_PRIVATE_KEY=PRIVATE_KEY
    JWT_PUBLIC_KEY=PUBLIC_KEY

    CACHE_TYPE="RedisCache"
    CACHE_REDIS_URL=os.getenv("CACHE_REDIS_URL")
    CACHE_DEFAULT_TIMEOUT=60