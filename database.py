from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///vet_vaccination.db')
Session = sessionmaker(bind=engine)

from models.animal import Animal
from models.owner import Owner
from models.vaccination import Vaccination