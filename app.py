from flask import Flask, render_template
from model import db

app = Flask(__name__)

@app.route("/")
def index():
    return "Ga naar /agenda voor de agenda."

@app.route("/agenda")
def agenda():
    return render_template("agenda.html")

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)