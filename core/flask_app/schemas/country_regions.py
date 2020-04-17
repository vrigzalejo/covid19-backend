from graphene_sqlalchemy import SQLAlchemyObjectType
from flask_app.models.country_regions import (
    CountryRegion as CountryRegionModel
)
import graphene


class CountryRegion(SQLAlchemyObjectType):
    class Meta:
        model = CountryRegionModel


class Query(graphene.ObjectType):
    country_regions = graphene.List(
        CountryRegion,
        country_region=graphene.String(),
        province_state=graphene.String()
    )

    def resolve_country_regions(
        self,
        info,
        country_region=None,
        province_state=None
    ):
        query = CountryRegion.get_query(info)

        if country_region:
            query = query.filter(
                CountryRegionModel.country_region == country_region
            )

        if province_state:
            query = query.filter(
                CountryRegionModel.province_state == province_state
            )

        return query.all()
