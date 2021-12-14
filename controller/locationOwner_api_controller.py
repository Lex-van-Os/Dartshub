from config import db
from models import user
from flask_restful import Resource, reqparse

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

class RestLocationOwner(Resource):
    def get(self, name):
        name_extra_params = name_pars.parse_args()
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
        
    def post(self, name):
        name_extra_params = name_pars.parse_args()
        current_user = user.query.filter_by(
            name=name,
            email=name_extra_params['email'],
            password=name_extra_params['password']).first()
        
        db.session.add(current_user)
        db.session.commit()
        
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
        
        if current_user == None:
            return {
                "Note": "Probaly already deleted or not found",
                "Status-code": "404",
            }, 404

        else:
            db.session.delete(current_user)
            db.session.commit()
            return {"note": "Succesfully deleted"}, 200