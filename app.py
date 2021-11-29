import os, json

from flask import Flask, render_template
from flask_migrate import Migrate
from datetime import datetime

import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, 'dartsbond.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from model import Event, db
mirgate = Migrate(app, db)

@app.route("/")
def index():
    return "Ga naar /agenda voor de agenda."

@app.route("/agenda")
def agenda():
    # Gets current date
    currentDate = datetime.today()
    
    # Get events with try and except
    try:
        # Get events
        events = db.session.query(Event).filter(Event.date >= currentDate).all()
    except SQLAlchemyError as e: # Error
        error = str(e.__dict__['orig'])
        return error
    finally:
        print(events)    
        
        # Use {{ eventData }} to acces event data in the front-end.
        return render_template("agenda.html", eventData=events)

if __name__ == "__main__":
    app.run(debug=True)