# imports for atm
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

# home dir app.py, this var is created to make a basedir for the sqlite file in this files contains our db..
BASE_DIR = os.path.dirname(os.path.abspath(__name__))

# create the flask app
app = Flask(__name__, template_folder="templates")

# configure the flask app
# configure the secret key later because if it is in plain text hackers can intercept data
app.config['SECRET_KEY'] = 'LaterDitVeranderenIVMsecurity'
app.config['FLASK_ENV'] = 'development'

# configure app to locate the resources of sqlite and his database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    BASE_DIR, 'database.sqlite')

# track db changes, can be turned on but it's resources intensive... so for now please let it be False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# creating instances
db = SQLAlchemy(app)
api = Api(app)
Migrate(app, db)

from routes import routing