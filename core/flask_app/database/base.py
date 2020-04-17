from flask_app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
from flask_app.models import (  # noqa: F401
    country_regions,
    confirmed_global,
    deaths_global,
    recovered_global
)  # noqa: E402

migrate = Migrate(app, db)
