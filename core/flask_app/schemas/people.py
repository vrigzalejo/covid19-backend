from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from flask_app.database.base import db
# from flask_app.models.people import People as PeopleModel
from flask_app.utils import input_to_dictionary
import graphene


class People(SQLAlchemyObjectType):
    """People node."""

    class Meta:
        # model = PeopleModel


class Query(graphene.ObjectType):
    # people = graphene.List(People)

    # def resolve_people(self, info):
    #     return PeopleModel.query.all()