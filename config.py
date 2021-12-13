# imports for atm
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager, login_manager
from flask_bcrypt import Bcrypt
from flask_dance.contrib.google import make_google_blueprint
import os

# LoginManager implementation
login_manager = LoginManager()

# home dir app.py, this var is created to make a basedir for the sqlite file in this files contains our db..
BASE_DIR = os.path.dirname(os.path.abspath(__name__))

# create the flask app
app = Flask(__name__, template_folder="templates")

# configure the flask app
# configure the secret key later because if it is in plain text hackers can intercept data
app.config[
    "SECRET_KEY"] = "21EA2DE8E6D06472E058E3E5F7E9AD3DB40A34B0A43AD5A3200F14797ADBF398"
app.config["FLASK_ENV"] = "development"

# configure app to locate the resources of sqlite and his database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    BASE_DIR, "database.sqlite")

# track db changes, can be turned on but it's resources intensive... so for now please let it be False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# CORS for AJAX calls
cors_user_api = CORS(
    app,
    resources={r"/api/v1/almere/user/*": {
        "origins": "*"
    }},
    methods=["GET", "POST", "DELETE"],
)
cors_admin_api = CORS(
    app,
    resources={r"/api/v1/almere/admin/*": {
        "origins": "*"
    }},
    methods=["GET", "POST", "DELETE"],
)

# instances
db = SQLAlchemy(app)
api = Api(app)
Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

# Google Login blueprint register
blueprint = make_google_blueprint(
    client_id=
    '865350764696-b57b9cp5igg8s4sr3bjn9stqfmccgnhu.apps.googleusercontent.com',
    client_secret='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',
    offline=True,
    scope=['profile', 'email'],
)
app.register_blueprint(blueprint, url_prefix='/login')
# Google login
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'

from routes import urls_api, routing
