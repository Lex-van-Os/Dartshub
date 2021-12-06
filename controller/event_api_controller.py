# modules for the rest api classes, model is imported to make connection with the sqlite tables and databases
from config import db
from models.event_model import Event
from models.event_model2 import EventAgenda
from flask_restful import Resource


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

        event = Event(name=name)
        db.session.add(event)
        db.session.commit()

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
            return {"note": "Succesfully deleted"}, 200


# trying to create the full functionality for the rest API
class RestEventsTwee(Resource):
    def get(self, name, date, time, desc, age):

        event = EventAgenda.query.filter_by(name=name, date=date).first()

        if event:
            return event.json()
        else:
            return {
                "Note": "Did not find resource(s)",
                "Status": "404",
                "Resource": None,
            }, 404

    def post(self, name, date, time, desc, age):

        event = EventAgenda(name=name, date=date, time=time, desc=desc, age=age)

        db.session.add(event)
        db.session.commit()

        return event.json()

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
