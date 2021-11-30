from app import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



"""
How to add new migrations? Via Terminal

Add a new migrations: flask db migrate -m "Description of migration"

Update the DB: flask db upgrade

For help: flask db --help
"""

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    date = db.Column(db.Text, unique=False, nullable=False)
    time = db.Column(db.Text, unique=False, nullable=False)
    desc = db.Column(db.String(248), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    
    def __init__(self, name, date, time, desc, age):
        self.name = name
        self.date = date
        self.time = time
        self.desc = desc
        self.age = age
    
    def __repr__(self):
        events = {
            "id" : self.id,
            "name" : self.name,
            "date" : self.date,
            "time" : self.time,
            "desc" : self.desc,
            "age" : self.age
        }
        return str(events)