# moduls to create the model
from config import db, login_manager
from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
"""
How to add new migrations? Via Terminal

Add a new migrations: flask db migrate -m "Description of migration"

Update the DB: flask db upgrade

For help: flask db --help

"""


# Model for the location owners.
# Defined data in this model, is automatically communicated to the database in the form of table data, done through SQL Alchemy
class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128))
    
    def json(self):
        return {
            "id" : self.id,
            "email" : self.email,
            "username" : self.username,
            "password" : self.password
        }
