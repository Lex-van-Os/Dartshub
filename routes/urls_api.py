from config import api
from controller.event_api_controller import (
    RestEvents,
    AdminAPI,
)
from controller.location_api_controller import RestLocation
from controller.locationOwner_api_controller import RestLocationOwner

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
    "/api/v2/almere/events/<string:name>",
)

################################

# LocationAPI URLs "<string:owner_name> will be later replace by some data from the forms, for now online testing and developing"
api.add_resource(
    RestLocationOwner,
    "/api/v2/almere/location/<string:owner_name>",
    endpoint="owner_name"
)

# AdminAPI URLs "<string:admin_name> will be later replace by some data from the forms, for now online testing and developing"
api.add_resource(
    AdminAPI,
    "/api/v1/almere/admin/<string:admin_name>",
    endpoint="admin_name",
)

# LocationAPI URLs "<string:location_name> will be later replace by some data from the forms, for now online testing and developing"
api.add_resource(
    RestLocation,
    "/api/v2/almere/location/<string:location_name>",
    endpoint="location_name"
)