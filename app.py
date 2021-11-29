# imports for atm
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Deze module gebruiken we straks voor onze REST_Api, ik zet het alvast hierin neer.
from flask_restful import Resource, Api

# home dir app.py, this var is created to make a basedir for the sqlite file in this files contains our db...
basedir = os.path.abspath(os.path.dirname(__file__))

# create the flask app
app = Flask(__name__)

# configure the flask app
# configure the secret key later because if it is in plain text hackers can intercept data
app.config['SECRET_KEY'] = 'LaterDitVeranderenIVMsecurity'
app.config['FLASK_ENV'] = 'development'

# configure app to locate the resources of sqlite and his database
app.config['SQLALCHELMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, 'database.sqlite')

# track db changes, can be turned on but it's resources intensive... so for now please let it be False
app.config['SQLALCHELMY_TRACK_MODIFICATIONS'] = False

# create db var to use it to query, create, delete, read and update tables models etc...
db = SQLAlchemy(app)

# with migrate we can upgrade our tables and models for this there are several instructions for it.
Migrate(app, db)


# Routes of the webpages
@app.route("/")
@app.route("/home")
def index():

    return render_template('index.html')


@app.route("/agenda")
def agenda():
    return render_template("agenda.html.jinja")


# run python/flask app
if __name__ == "__main__":

    # always true because so you can debug the application much easier... trust me
    app.run(debug=True)
