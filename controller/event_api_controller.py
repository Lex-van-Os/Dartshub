# modules for the rest api classes, model is imported to make connection with the sqlite tables and databases
from config import db
from models.event_model import Event
from datetime import datetime
from sqlalchemy import exc
from flask_restful import Resource, reqparse

# Setting up of event validation through RequestParser
name_pars = reqparse.RequestParser()
name_pars.add_argument("date",
                       type=str,
                       help="date is required",
                       required=True)
name_pars.add_argument("time",
                       type=int,
                       help="time is required",
                       required=True)
name_pars.add_argument("desc",
                       type=str,
                       help="desc is required",
                       required=True)
name_pars.add_argument(
    "age",
    type=int,
    help="age is required",
    required=True,
)


# event API class for defining and using API methods
class RestEvents(Resource):


    # Get event has been refactored to get an event based on id. This way, details of specific events can be loaded in
    def get(self, id):
        event = Event.query.get(id)

        if event:
            return event.json()
        else:
            return {
                "Note": "Did not find resource(s)",
                "Status": "404",
                "Resource": None,
            }, 404


    def post(self, name):
        # Extra fields besides name, are parsed so that these parameters don't have to be included inside of a POST URL
        name_extra_params = name_pars.parse_args()
        event = Event(name=name,
                      date=name_extra_params["date"],
                      time=name_extra_params["time"],
                      desc=name_extra_params["desc"],
                      age=name_extra_params["age"]) 

        # Saving of item to the database and later returning a HTTP code message
        db.session.add(event)
        db.session.commit()

        if event:
            return event.json(), 200
        else:
            return {
                "Note":
                "Could not POST resource(s), probably because wrong arguments or parameters were passed",
                "Status": "400",
                "Resource": None,
            }, 404

    def delete(self, name):

        event = Event.query.filter_by(name=name).first()

        # In case item does not exist, a 404 not found message is returned
        if event == None:
            return {
                "Note": "Requested item could not be found",
                "Status-code": "404",
            }, 404

        else:
            # Deleting of item incase item has been found
            db.session.delete(event)
            db.session.commit()
            return {"note": "Succesfully deleted"}, 200


# Admin API for the website administrator
class AdminAPI(Resource):
    def get(self, admin_name):

        return {"test": admin_name}

    def post(self, admin_name):

        return {"test": admin_name}

    def delete(self, admin_name):

        return {"test": admin_name}

    def put(self, admin_name):

        return {"test": admin_name}


# User API for the location owners
class UserAPI(Resource):
    def get(self, user_name):

        return {"test": user_name}

    def post(self, user_name):

        return {"test": user_name}

    def delete(self, user_name):

        return {"test": user_name}

    def put(self, user_name):

        return {"test": user_name}
