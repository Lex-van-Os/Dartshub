from config import api
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
