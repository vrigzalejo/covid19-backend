from flask_app.database.base import db
from .country_regions import CountryRegion
from datetime import datetime


class DeathsGlobal(db.Model):
    __tablename__ = 'deaths_global'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_region_id = db.Column(
        db.Integer,
        db.ForeignKey(CountryRegion.id),
        nullable=False
    )
    numbers = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    country_region = db.relationship(
        CountryRegion,
        backref=db.backref(__tablename__, lazy=True)
    )
