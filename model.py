import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, 'dartsbond.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    time = db.Column(db.Time, unique=False, nullable=False)
    desc = db.Column(db.String(248), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    
    def __init__(self, name, time, desc, age):
        self.name = name
        self.time = time
        self.desc = desc
        self.age = age
    
    def __repr__(self):
        return f"Event('{self.name}', '{self.time}', '{self.desc}', '{self.age}')"