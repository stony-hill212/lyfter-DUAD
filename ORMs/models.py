from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True)
    name=Column(String(100), nullable=False)
    email=Column(String(100), nullable=False, unique=True)
    addresses=relationship("Address", back_populates="user")
    cars=relationship("Car", back_populates="user")

class Address(Base):
    __tablename__="addresses"
    id=Column(Integer, primary_key=True)
    street=Column(String(100), nullable=False)
    user_id=Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    user=relationship("User", back_populates="addresses")

class Car(Base):
    __tablename__="cars"
    id=Column(Integer, primary_key=True)
    make=Column(String(50))
    model=Column(String(50))
    user_id=Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )
    user=relationship("User", back_populates="cars")