from config import app
from flask import render_template
from controller.event_api_controller import RestEventsTwee

# Routes of the webpages
@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html.jinja')


@app.route("/agenda")
def agenda():
    return render_template("agenda.html.jinja")


@app.route("/event/create", methods=['GET', 'POST'])
def form():
    return render_template("event/event_create.html.jinja")


# Loading the details page based on a specific id given to the page
@app.route("/event/details/<id>")
def details(id):
    eventsAPI = RestEventsTwee()
    event = eventsAPI.get(id) # Getting the event based on id
    return render_template("event/event_detail.html.jinja", event=event) # Passing the event so that event data can be dynamically loaded in jinja

    # Gets event name

    # The database we use to gather the information from forms: flaskwtforms

    # The form.html web page needs the backend to get the data from the form submitted
    # to be displayed to the user by sending them an email
    # POST & GET methods are required
