from flask_app.database.base import db


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(128))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
