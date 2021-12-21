# moduls to create the model
from sqlalchemy.orm import relationship
from config import db
from models import location_model
"""
How to add new migrations? Via Terminal

Add a new migrations: flask db migrate -m "Description of migration"

Update the DB: flask db upgrade

For help: flask db --help

BELANGRIJK: CHRIS IK HEB JE TABLE EEN BEETJE AANGEPAST ANDERS FUNCTIONEERT HIJ NIET MET DE API
"""


class Event(db.Model):

    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    date = db.Column(db.Text, unique=False, nullable=False)
    time = db.Column(db.Text, unique=False, nullable=False)
    desc = db.Column(db.String(248), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    locationID = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    location = relationship('Location', backref='events')

    def json(self):

        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "time": self.time,
            "desc": self.desc,
            "age": self.age,
        }
