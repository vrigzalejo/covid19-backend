from graphene import ObjectType, Schema
from .country_regions import (Query as QueryCountryRegion)
from .confirmed_global import (Query as QueryConfirmedGlobal)
from .deaths_global import (Query as QueryDeathsGlobal)
from .recovered_global import (Query as QueryRecoveredGlobal)


class Query(
    QueryCountryRegion,
    QueryConfirmedGlobal,
    QueryDeathsGlobal,
    QueryRecoveredGlobal,
    ObjectType
):
    pass


schema = Schema(query=Query)
