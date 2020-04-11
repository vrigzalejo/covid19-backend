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
    total_recovered_global = graphene.Int()

    def resolve_total_recovered_global(self, info):
        query = RecoveredGlobal.get_query(info)

        filter = (
            RecoveredGlobalModel.date == db.session.query(
                func.max(RecoveredGlobalModel.date),
            )
        )

        sum = 0
        for row in query.filter(filter):
            sum += row.numbers

        return sum

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
