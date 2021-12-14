# moduls to create the model
from config import db
from models import location_model
"""
How to add new migrations? Via Terminal

Add a new migrations: flask db migrate -m "Description of migration"

Update the DB: flask db upgrade

For help: flask db --help

BELANGRIJK: CHRIS IK HEB JE TABLE EEN BEETJE AANGEPAST ANDERS FUNCTIONEERT HIJ NIET MET DE API
"""


class EventAgenda(db.Model):

    __tablename__ = "events_agenda"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    date = db.Column(db.Text, unique=False, nullable=False)
    time = db.Column(db.Text, unique=False, nullable=False)
    desc = db.Column(db.String(248), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    locationID = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    user = db.relationship('Location', backref=db.backref('events_agenda'), lazy=True)

    def __init__(self, name="", date="", time="", desc="", age=""):
        self.name = name
        self.date = date
        self.time = time
        self.desc = desc
        self.age = age

    def init_db(self):
        db.create_all()

    # Ik heb dit gemaakt "Nilesh"
    def json(self):

        return {
            "name": self.name,
            "date": self.date,
            "time": self.time,
            "desc": self.desc,
            "age": self.age,
        }

    def __repr__(self):
        events = {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "time": self.time,
            "desc": self.desc,
            "age": self.age,
        }
        return str(events)
