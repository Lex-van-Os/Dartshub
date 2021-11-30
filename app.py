# imports for atm
from flask import Flask, render_template
from flask_migrate import Migrate
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import os

# home dir app.py, this var is created to make a basedir for the sqlite file in this files contains our db..
BASE_DIR = os.path.dirname(os.path.abspath(__name__))

# create the flask app
app = Flask(__name__)

# configure the flask app
# configure the secret key later because if it is in plain text hackers can intercept data
app.config['SECRET_KEY'] = 'LaterDitVeranderenIVMsecurity'
app.config['FLASK_ENV'] = 'development'

# configure app to locate the resources of sqlite and his database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, 'database.sqlite')

# track db changes, can be turned on but it's resources intensive... so for now please let it be False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create db var to use it to query, create, delete, read and update tables models etc...
db = SQLAlchemy(app)

# imports event form model
from model import Event
# with migrate we can upgrade our tables and models for this there are several instructions for it.
Migrate(app, db)

# Routes of the webpages
@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')

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
        return events
if __name__ == "__main__":
    app.run(debug=True)