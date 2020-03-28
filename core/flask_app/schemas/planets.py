from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from flask_app.database.base import db
from flask_app.models.planets import Planets as PlanetsModel
from flask_app.utils import input_to_dictionary
import graphene


# Create a generic class to mutualize description of planet attributes for both queries and mutations
class PlanetAttribute:
    name = graphene.String(description="Name of the planet.")
    rotation_period = graphene.String(description="Rotation period of the planet.")
    orbital_period = graphene.String(description="Orbital period of the planet.")
    diameter = graphene.String(description="Diameter of the planet.")
    climate = graphene.String(description="Climate period of the planet.")
    gravity = graphene.String(description="Gravity of the planet.")
    terrain = graphene.String(description="Terrain of the planet.")
    surface_water = graphene.String(description="Surface water of the planet.")
    population = graphene.String(description="Population of the planet.")
    url = graphene.String(description="URL of the planet in the Star Wars API.")


class Planet(SQLAlchemyObjectType):
    """Planet node."""

    class Meta:
        model = PlanetsModel
        interfaces = (graphene.relay.Node,)


class CreatePlanetInput(graphene.InputObjectType, PlanetAttribute):
    """Arguments to create a planet."""
    pass


class CreatePlanet(graphene.Mutation):
    """Create a planet."""
    planet = graphene.Field(lambda: Planet, description="Planet created by this mutation.")

    class Arguments:
        input = CreatePlanetInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        planet = PlanetsModel(**data)
        db.session.add(planet)
        db.session.commit()

        return CreatePlanet(planet=planet)


class UpdatePlanetInput(graphene.InputObjectType, PlanetAttribute):
    """Arguments to update a planet."""
    id = graphene.ID(required=True, description="Global Id of the planet.")


class UpdatePlanet(graphene.Mutation):
    """Update a planet."""
    planet = graphene.Field(lambda: Planet, description="Planet updated by this mutation.")

    class Arguments:
        input = UpdatePlanetInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        planet = db.session.query(PlanetsModel).filter_by(id=data['id'])
        planet.update(data)
        db.session.commit()
        planet = db.session.query(PlanetsModel).filter_by(id=data['id']).first()

        return UpdatePlanet(planet=planet)
        