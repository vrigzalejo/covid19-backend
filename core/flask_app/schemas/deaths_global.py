from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import (
    func
)
from flask_app.models.deaths_global import (
    DeathsGlobal as DeathsGlobalModel
)
from flask_app.database.base import db
import graphene


class DeathsGlobal(SQLAlchemyObjectType):
    class Meta:
        model = DeathsGlobalModel


class Query(graphene.ObjectType):
    deaths_global = graphene.List(
        DeathsGlobal,
        latest=graphene.Boolean()
    )

    def resolve_deaths_global(
        self,
        info,
        latest=None
    ):
        query = DeathsGlobal.get_query(info)

        if latest:
            filter = (
                DeathsGlobalModel.date == db.session.query(
                    func.max(DeathsGlobalModel.date)
                )
            )
            return query.filter(filter)

        return query.all()
