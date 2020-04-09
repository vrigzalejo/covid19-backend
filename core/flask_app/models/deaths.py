from flask_app.database.base import db
from .cases import Case
from datetime import datetime


class Death(db.Model):
    __tablename__ = 'deaths'
    id = db.Column(db.Integer, primary_key=True)
    numbers = db.Column(db.Integer)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    case = db.relationship(Case, backref=db.backref('deaths', lazy=True))
