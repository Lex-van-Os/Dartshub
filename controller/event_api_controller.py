# modules for the rest api classes, model is imported to make connection with the sqlite tables and databases
from config import db
from models.event_model import Event
from flask_restful import Resource
from datetime import datetime
from sqlalchemy import exc


# create a resource, with all "well at least DEL, GET and POST" HTTP methods
# this resource is connected with a API URL to function.
class RestEvents(Resource):
    def get(self, name):

        event = Event.query.filter_by(name=name).first()

        if event:
            return event.json()
        else:
            return {
                'Note': 'Did not find resource(s)',
                'Status': '404',
                "Resource": None
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
                'Note': 'Probaly already deleted or not found',
                "Status-code": '404'
            }, 404

        else:
            db.session.delete(event)
            db.session.commit()
            return {'note': 'Succesfully deleted'}, 200


    def get_future_events(self):
        currentDate = datetime.now().date()
        currentDateEu = f"{currentDate.day}-{currentDate.month}-{currentDate.year}"

        # Get events with try and except
        try:
            # Get events
            events = Event.query.filter(Event.date <= currentDateEu).all()
        except exc.SQLAlchemyError as e: # Error
            error = str(e.dict['orig'])
            return {
                'Note': error,
                'Status': '404',
                "Resource": None
            }, 404

        else:
            return events
