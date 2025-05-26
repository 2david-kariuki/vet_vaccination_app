from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Animal(Base):
    __tablename__ = 'animals'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    owner_id = Column(Integer, ForeignKey('owners.id'))