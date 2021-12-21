# modules for the rest api classes, model is imported to make connection with the sqlite tables and databases
from config import db
from models.location_model import Location
from flask_restful import Resource, reqparse

# Setting up of event validation through RequestParser
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

# Location API class for defining and using Location API methods
class RestLocation(Resource):

    #Location get method, that makes use of name and other extra parameters to retrieve information from the database
    def get(self, name):
        # Retrieval of extra parameters through parse_args(). This way, extra data doesn't have to be included in the URL
        name_extra_params = name_pars.parse_args()
        location = Location.query.filter_by(
            name=name,
            city=name_extra_params["city"],
            adress=name_extra_params["adress"],
            zipcode=name_extra_params["zipcode"],
            phonenumber=name_extra_params["phonenumber"],
            link=name_extra_params["link"]).first()
        
        if location:
            return location.json() # Returning of the location data through the location JSON method, to parse to json for returning
        else:
            return {
                "Note": "Did not find resource(s)",
                "Status": "404",
                "Resource": None,
            }, 404
    

    # Location post method, making use of the same parse_args() method as the GET to add a new Location to the database
    def post(self, name):
        name_extra_params = name_pars.parse_args()
        location = Location.query.filter_by(
            name=name,
            city=name_extra_params["city"],
            adress=name_extra_params["adress"],
            zipcode=name_extra_params["zipcode"],
            phonenumber=name_extra_params["phonenumber"],
            link=name_extra_params["link"]).first()
        
        # Adding new location to the database
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
    

    # Delete location to delete a location based on name
    def delete(self, name):
        location = Location.query.filter_by(name=name).first()
        
        # Return 404 incase location cannot be retrieved from the database
        if location == None:
            return {
                "Note": "Probaly already deleted or not found",
                "Status-code": "404",
            }, 404

        else:
            # Deleting of the database and returning HTTP 200 OK message
            db.session.delete(location)
            db.session.commit()
            return {"note": "Succesfully deleted"}, 200
