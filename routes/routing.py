from config import app
from flask import render_template


# Routes of the webpages
@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html.jinja')


@app.route("/agenda")
def agenda():
    return render_template("agenda.html.jinja")


@app.route("/event/create")
def form():
    return render_template("event/event_create.html.jinja")

@app.route("/create_event", methods=['GET', 'POST'])
def form():
    form = EventsForm(FlaskForm)
    return render_template("create_event.html", title="Create Event", form=form)

    # Gets event name

    # The database we use to gather the information from forms: flaskwtforms

    # The form.html web page needs the backend to get the data from the form submitted
    # to be displayed to the user by sending them an email
    # POST & GET methods are required
