from config import app
from flask import render_template

from forms.event_form import EventsForm
from forms.event_form import FlaskForm


# Routes of the webpages
@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html.jinja')


@app.route("/agenda")
def agenda():
    return render_template("agenda.html.jinja")


@app.route("/edit-event")
def edit_event():
    return render_template("event/event_edit.html.jinja")


@app.route("/create-event", methods=['GET', 'POST'])
def form():
    myForm = EventsForm()
    return render_template("event/event_create.html.jinja",
                           title="Create Event",
                           form=myForm)
    # Gets event name

    # The database we use to gather the information from forms: flaskwtforms

    # The form.html web page needs the backend to get the data from the form submitted
    # to be displayed to the user by sending them an email

@app.route("/events/location/detail")
def location_detail():
    return render_template("event/event_detail.html.jinja")

@app.route("/events")
def event():
    return render_template("events.html.jinja")