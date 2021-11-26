import os

from flask import Flask, render_template
from flask_migrate import Migrate

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, 'dartsbond.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from model import db
mirgate = Migrate(app, db)

@app.route("/")
def index():
    return "Ga naar /agenda voor de agenda."

@app.route("/agenda")
def agenda():
    return render_template("agenda.html")

if __name__ == "__main__":
    app.run(debug=True)