from flask.cli import AppGroup
import click

from collectors.manage import CrawlerManager
from models.onet import ONet_Manager

manager = AppGroup(help="Occupation management commands.")

@manager.command()
def print_stats():
    ONet_Manager.print_stats()

@manager.command()
@click.argument('name')
def find_all(name):
    occupations = ONet_Manager.find_occupations(name)
    print(occupations)

@manager.command()
@click.argument('name')
def find_one(name):
    occupations = ONet_Manager.find_occupations(name)
    print(occupations[0])