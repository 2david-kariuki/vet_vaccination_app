import click
from sqlalchemy.orm import sessionmaker
from database import engine, Base
from models.animal import Animal
from models.vaccination import Vaccination
from models.owner import Owner

Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('species')
@click.argument('owner_id', type=int)
def add_animal(name, species, owner_id):
    session = Session()
    animal = Animal(name=name, species=species, owner_id=owner_id)
    session.add(animal)
    session.commit()
    click.echo(f"Added animal: {name}")

if __name__ == '__main__':
    cli()