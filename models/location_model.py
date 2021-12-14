# moduls to create the model
from config import db

class Location(db.Model):

    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(248), unique=False, nullable=False)
    adress = db.Column(db.String(248), unique=False, nullable=False)
    zipcode = db.Column(db.String(8), unique=False, nullable=True)
    phonenumber = db.Column(db.Integer, unique=False, nullable=False)
    link = db.Column(db.String(248), unique=False, nullable=False)

    def json(self):

        return {
            "name" : self.name,
            "city" : self.city,
            "adress" : self.adress,
            "zipcode" : self.zipcode,
            "phonenumber" : self.phonenumber,
            "link" : self.link
        }

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
