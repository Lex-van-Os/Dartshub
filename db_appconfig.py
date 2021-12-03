# imports for atm
from flask import Flask, render_template, request, jsonify
# from flask_migrate import Migrate
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from calendar import monthrange
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    BASE_DIR, 'database.sqlite')

# track db changes, can be turned on but it's resources intensive... so for now please let it be False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create db var to use it to query, create, delete, read and update tables models etc...
db = SQLAlchemy(app)

# imports event form model
from model import Agenda

# with migrate we can upgrade our tables and models for this there are several instructions for it.
# Migrate(app, db)


# Function for retrieving events for database. Refactored, seeing how this may be used in multiple other functions
def get_events_from_db():

    currentDate = datetime.now().date()
    currentDateEu = f"{currentDate.day}-{currentDate.month}-{currentDate.year}"


"""
Chris belangrijk: 

- Ik heb dit stukje eruit gecomment en andere kleine stukje in dit code want ik niet wat het exact doet, plus model veranderd contacteer me om verder hiermee te gaan
BYEBYE <3
;)

"""

#  # Get events with try and except
#  try:
#      # Get events
#      events = Agenda.query.filter(Agenda.date <= currentDateEu).all()
#  except SQLAlchemyError as e:  # Error
#      error = str(e.__dict__['orig'])
#      return error
#  else:
#      return events


# Routes of the webpages
@app.route("/")
@app.route("/home")
def index():

    return render_template('index.html')


# Function for retrieving events through a request
@app.route("/get_events", methods=['GET'])
def get_events():

    # Events are retrieved and are then converted to a json format, using the model serialize property, by looping through all fields
    # events = get_events_from_db()
    # return jsonify([field.serialize for field in events])
    pass


# Function for loading the agenda page with the needed data
@app.route("/agenda")
def agenda():

    # now = datetime.now()

    # # Dictionary of returned data, so that multiple pieces of data can be returned to a page
    # # This context is WIP and might be discarded when agenda logic is completed through JQuery
    # context = {
    #     'eventData': get_events_from_db(),
    #     'days': monthrange(
    #         now.year,
    #         now.month)[1],  # Get all days of current month, for displaying
    #     'day_int': 1,
    # }

    # Use {{ context[{name of context item}] }} to acces context data in the front-end.
    return render_template("agenda.html.jinja")


@app.route("/form")
def form():
    return render_template("form.html")
