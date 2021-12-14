from config import app, db, bcrypt, login_manager

# from models.admin import AdminUsers
from models.user import User
from forms.login_form import LoginForm, RegisterForm
from flask_login import login_required, login_user, logout_user
from flask import render_template, redirect, url_for, flash, session
from flask_dance.contrib.google import google

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
@app.route("/edit-event")
def edit_event():
    return render_template("event/event_edit.html.jinja")


@app.route("/create-event", methods=["GET", "POST"])
def form():
    return render_template("event/event_create.html.jinja")


@app.route("/logout")
@login_required
def logout():

    if google.authorized:
        session.clear()
        return redirect("/agenda")

    logout_user()
    flash("U bent uitgelogt!")
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if google.authorized:

        resp = google.get("/oauth2/v2/userinfo")
        assert resp.ok, resp.text
        email = resp.json()["email"]
        user_google = User.query.filter_by(email=email).first()
        if user_google is None:
            user_google = User(email=email)
            db.session.add(user_google)
            db.session.commit()

        login_user(user_google)

        return redirect(url_for("welcome_google"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("welcome_user"))

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(
            email=form.email.data, username=form.username.data, password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login/google")
def login_google():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text

    return redirect(url_for("agenda"))


@app.route("/welcome/google")
@login_required
def welcome_google():

    if google.authorized:

        resp = google.get("/oauth2/v2/userinfo")
        assert resp.ok, resp.text
        email = resp.json()["email"]

    return render_template("welcome_user_google.html", email=email)


@app.route("/welcome")
@login_required
def welcome_user():
    return render_template("welcome_user.html")


@app.route("/events/location/detail")
def location_detail():
    return render_template("event/event_detail.html.jinja")

@app.route("/events")
def event():
    return render_template("events.html.jinja")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
