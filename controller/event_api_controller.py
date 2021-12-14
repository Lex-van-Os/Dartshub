# modules for the rest api classes, model is imported to make connection with the sqlite tables and databases
from config import db
from models.event_model import Event
from models.event_model2 import EventAgenda
from datetime import datetime
from sqlalchemy import exc
from flask_restful import Resource, reqparse

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


# create a resource, with all "well at least DEL, GET and POST" HTTP methods
# this resource is connected with a API URL to function.
class RestEvents(Resource):
    def get(self, name):

        event = Event.query.filter_by(name=name).first()

        if event:
            return event.json()
        else:
            return {
                "Note": "Did not find resource(s)",
                "Status": "404",
                "Resource": None,
            }, 404


    def post(self, name):
        print("post")

        event = Event(name=name)
        db.session.add(event)
        db.session.commit()
        events = Event.query.all()
        print(events)

        return event.json()


    def delete(self, name):

        event = Event.query.filter_by(name=name).first()

        if event == None:
            return {
                "Note": "Probaly already deleted or not found",
                "Status-code": "404",
            }, 404

        else:
            db.session.delete(event)
            db.session.commit()
            return {'note': 'Succesfully deleted'}, 200


# trying to create the full functionality for the rest API
class RestEventsTwee(Resource):


    # Get event has been refactored to get an event based on id. This way, details of specific events can be loaded in
    def get(self, id):
        event = EventAgenda.query.get(id)

        if event:
            return event.json()
        else:
            return {
                "Note": "Did not find resource(s)",
                "Status": "404",
                "Resource": None,
            }, 404

    def post(self, name):
        print("POST")
        name_extra_params = name_pars.parse_args()
        event = EventAgenda(name=name,
                            date=name_extra_params["date"],
                            time=name_extra_params["time"],
                            desc=name_extra_params["desc"],
                            age=name_extra_params["age"])


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

        event = EventAgenda.query.filter_by(name=name).first()

        if event == None:
            return {
                "Note": "Probaly already deleted or not found",
                "Status-code": "404",
            }, 404

        else:
            db.session.delete(event)
            db.session.commit()
            return {"note": "Succesfully deleted"}, 200


    # Function for retrieving all future events for the agenda page and possibly other future pages.
    # This function is yet to be converted to a API function. This serves as a template to lookup the needed functionality for the new function
    
    # def get_future_events(self):
    #     currentDate = datetime.now().date()
    #     currentDateEu = f"{currentDate.day}-{currentDate.month}-{currentDate.year}"

    #     # Get events with try and except
    #     try:
    #         # Get events
    #         events = Event.query.filter(Event.date <= currentDateEu).all()
    #     except exc.SQLAlchemyError as e: # Error
    #         error = str(e.dict['orig'])
    #         return {
    #             'Note': error,
    #             'Status': '404',
    #             "Resource": None
    #         }, 404

    #     else:
    #         return events


class AdminAPI(Resource):
    def get(self, admin_name):

        return {"test": admin_name}

    def post(self, admin_name):

        return {"test": admin_name}

    def delete(self, admin_name):

        return {"test": admin_name}

    def put(self, admin_name):

        return {"test": admin_name}


class UserAPI(Resource):
    def get(self, user_name):

        return {"test": user_name}

    def post(self, user_name):

        return {"test": user_name}

    def delete(self, user_name):

        return {"test": user_name}

    def put(self, user_name):

        return {"test": user_name}
