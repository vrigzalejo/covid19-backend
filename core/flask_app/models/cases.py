from flask_app.database.base import db
from .countries import Country
from datetime import datetime


class Case(db.Model):
    __tablename__ = 'cases'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    country = db.relationship(Country, backref=db.backref('cases', lazy=True))
