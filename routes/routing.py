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
def create_event():
    return render_template("event/event_create.html.jinja")


@app.route("/event/edit")
def edit_event():
    return render_template("event/event_edit.html.jinja")
