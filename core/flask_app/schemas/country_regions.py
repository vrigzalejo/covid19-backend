from graphene_sqlalchemy import SQLAlchemyObjectType
from flask_app.models.country_regions import (
    CountryRegion as CountryRegionModel
)
import graphene


class CountryRegion(SQLAlchemyObjectType):
    class Meta:
        model = CountryRegionModel


class Query(graphene.ObjectType):
    country_regions = graphene.List(CountryRegion)

    def resolve_country_regions(self, info):
        return CountryRegionModel.query.all()
