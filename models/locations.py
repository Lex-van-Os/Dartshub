# moduls to create the model
from config import db
"""
How to add new migrations? Via Terminal

Add a new migrations: flask db migrate -m "Description of migration"

Update the DB: flask db upgrade

For help: flask db --help

"""


# Model for the event location.
# Defined data in this model, is automatically communicated to the database in the form of table data, done through SQL Alchemy
class Location(db.Model):

    __tablename__ = "Locations"
    id = db.Column(db.Integer, primary_key=True)
    name_location = db.Column(db.String(255), nullable=False, unique=False)
    location_adress = db.Column(db.String(255), nullable=False)
    # date = db.Column(db.datetime, default=datetime.datetime, unique=False)  ## Dit is een manier om automatisch time te inserten moet nog overleggen hierover ##
    opt_phone_number = db.Column(db.Integer, unique=False)

    def __init__(self, name_location, location_adress, opt_phone_number):

        self.name_location = name_location
        self.location_adress = location_adress
        self.opt_phone_number = opt_phone_number

    # Function for parsing location data to JSON format, for returning to the front-end
    def json(self):
        return {
            "name_location": self.name_location,
            "location_adress": self.location_adress,
            "opt_phone_number": self.opt_phone_number
        }
