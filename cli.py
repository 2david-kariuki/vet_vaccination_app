import click
from sqlalchemy.orm import sessionmaker
from database import engine, Base
from models.animal import Animal
from models.vaccination import Vaccination
from models.owner import Owner
from utils import validate_date

Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('contact')
def add_owner(name, contact):
    session = Session()
    owner = Owner(name=name, contact=contact)
    session.add(owner)
    session.commit()
    click.echo(f"Added owner: {name} (ID: {owner.id})")

@cli.command()
@click.argument('name')
@click.argument('species')
@click.argument('owner_id', type=int)
def add_animal(name, species, owner_id):
    session = Session()
    owner = session.query(Owner).get(owner_id)
    if not owner:
        click.echo(f"Error: Owner with ID {owner_id} does not exist")
        return
    animal = Animal(name=name, species=species, owner_id=owner_id)
    session.add(animal)
    session.commit()
    click.echo(f"Added animal: {name} (ID: {animal.id})")

@cli.command()
@click.argument('vaccine_type')
@click.argument('date')
@click.argument('animal_id', type=int)
def add_vaccination(vaccine_type, date, animal_id):
    session = Session()
    animal = session.query(Animal).get(animal_id)
    if not animal:
        click.echo(f"Error: Animal with ID {animal_id} does not exist")
        return
    try:
        validated_date = validate_date(date)
    except ValueError as e:
        click.echo(f"Error: {e}")
        return
    vaccination = Vaccination(vaccine_type=vaccine_type, date=validated_date, animal_id=animal_id)
    session.add(vaccination)
    session.commit()
    click.echo(f"Added vaccination: {vaccine_type} for animal ID {animal_id}")

@cli.command()
def list_animals():
    session = Session()
    animals = session.query(Animal).all()
    if not animals:
        click.echo("No animals found")
        return
    for animal in animals:
        click.echo(f"ID: {animal.id}, Name: {animal.name}, Species: {animal.species}, Owner ID: {animal.owner_id}")

if __name__ == '__main__':
    cli()