from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import (
    func
)
from flask_app.models.recovered_global import (
    RecoveredGlobal as RecoveredGlobalModel
)
from flask_app.database.base import db
import graphene


class RecoveredGlobal(SQLAlchemyObjectType):
    class Meta:
        model = RecoveredGlobalModel


class Query(graphene.ObjectType):
    recovered_global = graphene.List(
        RecoveredGlobal,
        latest=graphene.Boolean()
    )

    def resolve_recovered_global(
        self,
        info,
        latest=None
    ):
        query = RecoveredGlobal.get_query(info)

        if latest:
            filter = (
                RecoveredGlobalModel.date == db.session.query(
                    func.max(RecoveredGlobalModel.date)
                )
            )
            return query.filter(filter)

        return query.all()
