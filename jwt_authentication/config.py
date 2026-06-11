import os
from dotenv import load_dotenv

load_dotenv()

with open("private.pem", "r")as f:
        PRIVATE_KEY=f.read()
with open("public.pem", "r")as f:
        PUBLIC_KEY=f.read()

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_ALGORITHM="RS256"
    JWT_PRIVATE_KEY=PRIVATE_KEY
    JWT_PUBLIC_KEY=PUBLIC_KEY