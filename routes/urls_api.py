from config import api
from flask_restful import reqparse
from controller.event_api_controller import (
    RestEvents,
    RestEventsTwee,
    UserAPI,
    AdminAPI,
)

################################
"""
Below URLs for the APIs to make CRUD actions
Once the whole app is in running mode, the URLs will constantly listen to incoming HTTP verbs.

Goodluck devs :)
"""
################################

# test API but later for CRUD "events"
api.add_resource(
    RestEvents,
    "/api/v1/almere/events/<string:name>",
    endpoint="name",
)

name_pars = reqparse.RequestParser()
name_pars.add_argument("date", type=int, help="date is required", required=True)
name_pars.add_argument("time", type=int, help="time is required", required=True)
name_pars.add_argument("desc", type=int, help="desc is required", required=True)
name_pars.add_argument("age", type=int, help="age is required", required=True)
name_params = name_pars.parse_args()

api.add_resource(
    RestEventsTwee,
    "/api/v2/almere/events/<string:name>",
)

################################

# UserAPI URLs "<string:name> will be later replace by some data from the forms, for now online testing and developing"
api.add_resource(
    UserAPI,
    "/api/v1/almere/user/<string:user_name>",
    endpoint="user_name",
)

# AdminAPI URLs "<string:admin_name> will be later replace by some data from the forms, for now online testing and developing"
api.add_resource(
    AdminAPI,
    "/api/v1/almere/admin/<string:admin_name>",
    endpoint="admin_name",
)
