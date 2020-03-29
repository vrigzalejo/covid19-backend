from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene import ObjectType, String, Schema
from .planets import (Planet, Query as QueryPlanets)
from .people import (People, Query as QueryPeople)



class Query(
    QueryPlanets,
    QueryPeople,
    ObjectType
):
    pass


schema = Schema(query=Query)