from ast import literal_eval
from flask_app.models.people import People as PeopleModel
from flask_app.models.planets import Planets as PlanetsModel
from flask_app.database.base import db
import logging
import sys
import os

dataDir = os.path.abspath(os.path.dirname(__file__) + '/database/data/')

# Load logging configuration
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def seed():
    log.info('Insert Planets data in database')
    with open(os.path.join(dataDir, 'planets.json'), 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            planet = PlanetsModel(**record)
            log.info(planet)
            db.session.add(planet)
        db.session.commit()

    log.info('Insert People data in database')
    with open(os.path.join(dataDir, 'people.json'), 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            people = PeopleModel(**record)
            log.info(people)
            db.session.add(people)
        db.session.commit()
