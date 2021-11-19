from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Ga naar /agenda voor de agenda."

@app.route("/agenda")
def agenda():
    return render_template("agenda.html")