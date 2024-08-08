from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from app import db


class User(db.Model):
    __tablename__ = 'users'
    email = Column(String(20), primary_key=True)
    name = Column(String(20), nullable=False)
    role = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    
    @staticmethod
    def register_user(email, name, role, password):
        user = User(email=email, name=name, role=role, password=password)
        db.session.add(user)
        db.session.commit()
        return user

class Datasets(db.Model):
    __tablename__ = 'datasets'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(String(20), nullable=False)
    url = Column(String(20), nullable=False)
    owner = Column(String(20), nullable=True)
    