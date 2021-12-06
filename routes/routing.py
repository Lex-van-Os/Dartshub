from config import app, api
from flask_migrate import Migrate
from flask import render_template, request
from controller.event_api_controller import RestEvents


# Routes of the webpages
@app.route("/")
@app.route("/home")
def index():

    return render_template('home.html.jinja')


@app.route("/agenda")
def agenda():
    return render_template("agenda.html.jinja")


@app.route("/form")
def form():
    return render_template("form.html")


api.add_resource(RestEvents, '/api/almere/events/<string:name>')
