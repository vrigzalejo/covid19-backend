from flask_sqlalchemy import SQLAlchemy
from flask_app import app
from flask_migrate import Migrate

db = SQLAlchemy(app)
from flask_app.models import cases, countries, deaths, recoveries


migrate = Migrate(app, db)
