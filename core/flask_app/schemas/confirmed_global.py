from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import (
    func
)
from flask_app.models.confirmed_global import (
    ConfirmedGlobal as ConfirmedGlobalModel
)
from flask_app.database.base import db
import graphene


class ConfirmedGlobal(SQLAlchemyObjectType):
    class Meta:
        model = ConfirmedGlobalModel


class Query(graphene.ObjectType):
    confirmed_global = graphene.List(
        ConfirmedGlobal,
        latest=graphene.Boolean()
    )
    total_confirmed_global = graphene.Int()

    def resolve_total_confirmed_global(self, info):
        query = ConfirmedGlobal.get_query(info)

        filter = (
            ConfirmedGlobalModel.date == db.session.query(
                func.max(ConfirmedGlobalModel.date),
            )
        )

        sum = 0
        for row in query.filter(filter):
            sum += row.numbers

        return sum

    def resolve_confirmed_global(
        self,
        info,
        latest=None
    ):
        query = ConfirmedGlobal.get_query(info)

        if latest:
            filter = (
                ConfirmedGlobalModel.date == db.session.query(
                    func.max(ConfirmedGlobalModel.date)
                )
            )
            query = query.filter(filter)

        return query.all()
