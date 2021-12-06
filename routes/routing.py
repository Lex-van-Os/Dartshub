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


@app.route("/form")
def form():
    return render_template("form.html")
