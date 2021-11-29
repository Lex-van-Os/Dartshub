from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return "Ga naar /agenda voor de agenda."


@app.route("/test")
def test():
    return render_template("test.html.jinja")


@app.route("/agenda")
def agenda():
    return render_template("agenda.html.jinja")


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
