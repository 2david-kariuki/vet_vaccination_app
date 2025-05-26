from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base
from datetime import date

class Vaccination(Base):
    __tablename__ = 'vaccinations'
    id = Column(Integer, primary_key=True)
    vaccine_type = Column(String, nullable=False)
    date = Column(Date, default=date.today)
    animal_id = Column(Integer, ForeignKey('animals.id'), nullable=False)