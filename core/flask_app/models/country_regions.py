from flask_app.database.base import db


class CountryRegion(db.Model):
    __tablename__ = 'country_regions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    province_state = db.Column(db.String(128))
    country_region = db.Column(db.String(128))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
