from flask_app.database.base import db
from .countries import Country


class Province(db.Model):
    __tablename__ = 'provinces'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    province_state = db.Column(db.String(128))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    country = db.relationship(Country, backref=db.backref('provinces', lazy=True))
