import os

from flask import Flask, render_template
from flask_migrate import Migrate
from datetime import datetime
import calendar

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, 'dartsbond.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from model import Event, db
mirgate = Migrate(app, db)

@app.route("/")
def index():
    return "Ga naar /agenda voor de agenda."

@app.route("/agenda")
def agenda():
    currentDate = datetime.today()
    endDate = calendar.monthrange(currentDate.year, currentDate.month)[1]
    events = db.session.query(Event).filter(Event.date >= currentDate, Event.date <= endDate).all()
    
    print(events)
    return render_template("agenda.html")

if __name__ == "__main__":
    app.run(debug=True)