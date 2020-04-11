from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import (
    or_,
    and_
)
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
        
        if country_region or province_state:
            filter = (
                and_(
                    CountryRegionModel.country_region == country_region,
                    CountryRegionModel.province_state == province_state
                )
            )
            return query.filter(filter)

        return query.all()
