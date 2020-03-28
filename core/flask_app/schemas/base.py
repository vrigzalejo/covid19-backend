from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
from .planets import (Planet, CreatePlanet, UpdatePlanet)
from .people import (People, CreatePerson, UpdatePerson)


class Query(graphene.ObjectType):
    """Nodes which can be queried by this API."""
    node = graphene.relay.Node.Field()

    # People
    people = graphene.relay.Node.Field(People)
    peopleList = SQLAlchemyConnectionField(People)

    # Planets
    planets = graphene.relay.Node.Field(Planet)
    planetList = SQLAlchemyConnectionField(Planet)


class Mutation(graphene.ObjectType):
    """Mutations which can be performed by this API."""
    # Person mutation
    createPerson = CreatePerson.Field()
    updatePerson = UpdatePerson.Field()

    # Planet mutations
    createPlanet = CreatePlanet.Field()
    updatePlanet = UpdatePlanet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)