# modules for the rest api classes, model is imported to make connection with the sqlite tables and databases
from config import db
from models.location_model import Location
from flask_restful import Resource, reqparse

name_pars = reqparse.RequestParser()
name_pars.add_argument(
    "city",
    type=str,
    help="city is required",
    required=True
)
name_pars.add_argument(
    "adress",
    type=str,
    help="adress is required",
    required=True
)
name_pars.add_argument(
    "zipcode",
    type=str,
    help="zipcode is required",
    required=True
)
name_pars.add_argument(
    "phonenumber",
    type=str,
    help="phonenumber is required",
    required=True
)
name_pars.add_argument(
    "link",
    type=str,
    help="link is required",
    required=True
)

class RestLocation(Resource):
    def get(self, name):
        name_extra_params = name_pars.parse_args()
        location = Location.query.filter_by(
            name=name,
            city=name_extra_params["city"],
            adress=name_extra_params["adress"],
            zipcode=name_extra_params["zipcode"],
            phonenumber=name_extra_params["phonenumber"],
            link=name_extra_params["link"]).first()
        
        if location:
            return location.json()
        else:
            return {
                "Note": "Did not find resource(s)",
                "Status": "404",
                "Resource": None,
            }, 404
    
    def post(self, name):
        name_extra_params = name_pars.parse_args()
        location = Location.query.filter_by(
            name=name,
            city=name_extra_params["city"],
            adress=name_extra_params["adress"],
            zipcode=name_extra_params["zipcode"],
            phonenumber=name_extra_params["phonenumber"],
            link=name_extra_params["link"]).first()
        
        db.session.add(location)
        db.session.commit()
        
        if location:
            return location.json(), 200
        else:
            return {
                "Note":
                "Could not POST resource(s), probably because wrong arguments or parameters were passed",
                "Status": "400",
                "Resource": None,
            }, 404
    
    def delete(self, name):
        location = Location.query.filter_by(name=name).first()
        
        if location == None:
            return {
                "Note": "Probaly already deleted or not found",
                "Status-code": "404",
            }, 404

        else:
            db.session.delete(location)
            db.session.commit()
            return {"note": "Succesfully deleted"}, 200
