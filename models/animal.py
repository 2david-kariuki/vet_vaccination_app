from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Animal(Base):
    __tablename__ = 'animals'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)