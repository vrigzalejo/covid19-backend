from graphene_sqlalchemy import SQLAlchemyObjectType
from flask_app.models.recovered_global import (
    RecoveredGlobal as RecoveredGlobalModel
)
import graphene


class RecoveredGlobal(SQLAlchemyObjectType):
    class Meta:
        model = RecoveredGlobalModel


class Query(graphene.ObjectType):
    recovered_global = graphene.List(RecoveredGlobal)

    def resolve_recovered_global(self, info):
        query = RecoveredGlobal.get_query(info)
        return query.all()
