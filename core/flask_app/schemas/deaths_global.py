from graphene_sqlalchemy import SQLAlchemyObjectType
from flask_app.models.deaths_global import (
    DeathsGlobal as DeathsGlobalModel
)
import graphene


class DeathsGlobal(SQLAlchemyObjectType):
    class Meta:
        model = DeathsGlobalModel


class Query(graphene.ObjectType):
    deaths_global = graphene.List(DeathsGlobal)

    def resolve_deaths_global(self, info):
        return DeathsGlobalModel.query.all()
