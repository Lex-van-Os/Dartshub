# moduls to create the model
from config import db
from flask_login import UserMixin
"""
How to add new migrations? Via Terminal

Add a new migrations: flask db migrate -m "Description of migration"

Update the DB: flask db upgrade

For help: flask db --help

"""


# Model for the website admin user.
# Defined data in this model, is automatically communicated to the database in the form of table data, done through SQL Alchemy
class AdminUsers(UserMixin, db.Model):

    __tablename__ = 'admin_users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False, unique=False)
    last_name = db.Column(db.String(50), nullable=False, unique=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(255), nullable=False, unique=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, first_name, last_name, email, user_name, password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
        self.password = password

    def __repr__(self):
        # Returning of custom user info string when printing an admin user instance
        return f"User, ({self.first_name}, {self.last_name}, {self.email}, {self.password}) and his username is: {self.user_name}"

    # Function for parsing admin user data to JSON format, for returning to the front-end
    def json(self):

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "user_name": self.user_name,
            "password": self.password
        }