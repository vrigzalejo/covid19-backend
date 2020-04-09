from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from flask_app.database.base import db
# from flask_app.models.planets import Planets as PlanetsModel
from flask_app.utils import input_to_dictionary
import graphene


# Create a generic class to mutualize description of planet attributes for both queries and mutations
class Planet(SQLAlchemyObjectType):
    # """Planet node."""

    # class Meta:
    #     model = PlanetsModel

class Query(graphene.ObjectType):
    # planets = graphene.List(Planet)

    # def resolve_planets(self, info):
    #     return PlanetsModel.query.all()
