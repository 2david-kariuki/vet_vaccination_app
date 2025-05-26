from sqlalchemy import Column, Integer, String
from database import Base

class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)