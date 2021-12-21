# moduls to create the model
from config import db


# Model for the event location.
# Defined data in this model, is automatically communicated to the database in the form of table data, done through SQL Alchemy
class Location(db.Model):

    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(248), unique=False, nullable=False)
    adress = db.Column(db.String(248), unique=False, nullable=False)
    zipcode = db.Column(db.String(8), unique=False, nullable=True)
    phonenumber = db.Column(db.Integer, unique=False, nullable=False)
    link = db.Column(db.String(248), unique=False, nullable=False)


    def __init__(self, name="", city="", adress="", zipcode="", phonenumber=None, link=""):
        self.name = name
        self.city = city
        self.adress = adress
        self.zipcode = zipcode
        self.phonenumber = phonenumber
        self.link = link


    # Function for parsing location data to JSON format, for returning to the front-end
    def json(self):

        return {
            "name" : self.name,
            "city" : self.city,
            "adress" : self.adress,
            "zipcode" : self.zipcode,
            "phonenumber" : self.phonenumber,
            "link" : self.link
        }

    # Function for creating a custom print message incase of printing a location instance
    # Print is set up in JSON format, for better readability
    def __repr__(self):
        location = {
            "name" : self.name,
            "city" : self.city,
            "adress" : self.adress,
            "zipcode" : self.zipcode,
            "phonenumber" : self.phonenumber,
            "link" : self.link
        }
        return str(location)
