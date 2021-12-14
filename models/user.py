# moduls to create the model
from config import db, login_manager
from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
"""
How to add new migrations? Via Terminal

Add a new migrations: flask db migrate -m "Description of migration"

Update the DB: flask db upgrade

For help: flask db --help

BELANGRIJK: CHRIS IK HEB JE TABLE EEN BEETJE AANGEPAST ANDERS FUNCTIONEERT HIJ NIET MET DE API
"""


class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128))
