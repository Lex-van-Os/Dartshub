from flask.helpers import url_for
from config import app
from flask import render_template, request, redirect

# Routes of the webpages http://127.0.0.1:5000/
@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html.jinja")


# http://127.0.0.1:5000/agenda
@app.route("/agenda")
def agenda():
    return render_template("agenda.html.jinja")


# http://127.0.0.1:5000/event/event_create
@app.route("/event/event_create")
def event_create():
    return render_template("/event/event_create.html.jinja")

    # Dit meot nog
    # , methods=["POST"]
    # if request.method == "POST":
    #     event_detail = request.form[
    #         "date", "time", "event_category", "location", "phone_number"
    #      ]
    #     return redirect(request(url_for)"" = detail)
    # else:


# @app.route("/event/detail")
# def detail():
#     return f""


# @app.route("/<event/detail>")
# def event_detail():
#     return f"<h1>{idk yet}</h1>"
#     return render_template("event/event_detail.html.jinja")


# @app.route("/create_event", methods=["GET", "POST"])
# def form():
#     form = EventsForm(FlaskForm)
#     return render_template("create_event.html", title="Create Event", form=form)

# Gets event name

# The database we use to gather the information from forms: flaskwtforms

# The form.html web page needs the backend to get the data from the form submitted
# to be displayed to the user by sending them an email
# POST & GET methods are required
