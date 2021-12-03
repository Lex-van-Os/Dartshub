# These are the modules that will help to run the whole application
from db_appconfig import app, db
from flask_restful import Api
from flask_migrate import Migrate
from rest_class import RestEvents

# create instances and the migrate
api = Api(app)
Migrate(app, db)

# test api URL for api testing
api.add_resource(RestEvents, '/api/almere/events/<string:name>')

# run the application
if __name__ == '__main__':
    # db create is to create the tables. NOTE: im still looking for a other to remove this functions
    # but this will also work for now...
    db.create_all()
    app.run(debug=True)
