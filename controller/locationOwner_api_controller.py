from config import db
from models import user
from flask_restful import Resource, reqparse

# Defining of form validation through RequestParser
name_pars = reqparse.RequestParser()
name_pars.add_argument(
    "email",
    type=str,
    help="email is required",
    required=True
)
name_pars.add_argument(
    "password",
    type=str,
    help="password is required",
    required=True
)


# LocationOwner API for the location owners
class RestLocationOwner(Resource):

    # Getting a location based on name and other extra parameters
    def get(self, name):
        name_extra_params = name_pars.parse_args() # Defining of extra parameters through parse_args() so data doesn't have to be passed directly through an URL
        current_user = user.query.filter_by(
            name=name,
            email=name_extra_params['email'],
            password=name_extra_params['password']).first()

        if current_user:
            return current_user.json()
        else:
            return {
                "Note": "Did not find resource(s)",
                "Status": "404",
                "Resource": None,
            }, 404
        

    # Adding a location owner to the database, making use of the same parse_args()
    def post(self, name):
        name_extra_params = name_pars.parse_args()
        current_user = user.query.filter_by(
            name=name,
            email=name_extra_params['email'],
            password=name_extra_params['password']).first()
        
        db.session.add(current_user)
        db.session.commit()
        
        # Parsing the added location owner data to JSON, returning it and returning with it a status OK message
        if current_user:
            return current_user.json(), 200
        else:
            return {
                "Note":
                "Could not POST resource(s), probably because wrong arguments or parameters were passed",
                "Status": "400",
                "Resource": None,
            }, 404
    
    def delete(self, name):
        current_user = user.query.filter_by(name=name).first()
        
        # Returning 404 incase a given location owner cannot be retrieved from the database
        if current_user == None:
            return {
                "Note": "Probaly already deleted or not found",
                "Status-code": "404",
            }, 404

        # Deleting a location owner and returning a OK status message
        else:
            db.session.delete(current_user)
            db.session.commit()
            return {"note": "Succesfully deleted"}, 200