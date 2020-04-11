from graphene_sqlalchemy import SQLAlchemyObjectType
from flask_app.models.confirmed_global import (
    ConfirmedGlobal as ConfirmedGlobalModel
)
import graphene


class ConfirmedGlobal(SQLAlchemyObjectType):
    class Meta:
        model = ConfirmedGlobalModel


class Query(graphene.ObjectType):
    confirmed_global = graphene.List(ConfirmedGlobal)

    def resolve_confirmed_global(self, info):
        return ConfirmedGlobalModel.query.all()
