from config import app
from controller.event_api_controller import RestEvents
from config import app, db, bcrypt, login_manager
from models.user import User
from forms.login_form import LoginForm, RegisterForm
from flask_login import login_required, login_user, logout_user
from flask import render_template, redirect, url_for, flash, session
from flask_dance.contrib.google import google

# File for defining the routes of the website, for the website pages
# Needed functionality for certain pages, is communicated through the corresponding functions and returned in the render_template


# Routes of the webpages http://127.0.0.1:5000/
@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html.jinja")


# http://127.0.0.1:5000/agenda
@app.route("/agenda")
def agenda():
    return render_template("agenda.html.jinja")


# Loading the details page based on a specific id given to the page
@app.route("/event/details/<id>")
def details(id):
    eventsAPI = RestEvents()
    event = eventsAPI.get(id) # Getting the event based on id
    return render_template("event/event_detail.html.jinja", event=event) # Passing the event so that event data can be dynamically loaded in jinja


# http://127.0.0.1:5000/event/event_create
@app.route("/event/event_create")
def event_create():
    return render_template("/event/event_create.html.jinja")

    # This is yet to be implemented
    # , methods=["POST"]
    # if request.method == "POST":
    #     event_detail = request.form[
    #         "date", "time", "event_category", "location", "phone_number"
    #      ]
    #     return redirect(request(url_for)"" = detail)
    # else:


@app.route("/edit-event")
def edit_event():
    return render_template("event/event_edit.html.jinja")


# Route for location owner logout. In this function, google authorisation is checked to clear certain Google login sesssions
@app.route("/logout")
@login_required
def logout():

    # Clearing session incase of Google login authorisation
    if google.authorized:
        session.clear()
        return redirect("/agenda")


    # Calling of the util logout_user() function to logout
    logout_user()
    flash("U bent uitgelogt!")
    return redirect(url_for("login"))


# Route for logging in as location owner. Incase a user logs in using a Google account, specific functionality is executed
@app.route("/login", methods=["GET", "POST"])
def login():

    # Setting session and routing in case of Google user login
    if google.authorized:

        resp = google.get("/oauth2/v2/userinfo") # Getting information of Google account to store info as session
        assert resp.ok, resp.text
        email = resp.json()["email"]
        user_google = User.query.filter_by(email=email).first()

        # Storing Google user information for remember me functionality
        if user_google is None:
            user_google = User(email=email)
            db.session.add(user_google)
            db.session.commit()

        login_user(user_google)

        return redirect(url_for("welcome_google"))

    # Validating of form when logging in
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # Hashing of password when logging in
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("welcome_user"))

    return render_template("login.html", form=form)


# Route for the user register page. Entered password is automatically hashed when posting
@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()
    # Validate then hash password
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(
            email=form.email.data, username=form.username.data, password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


# Route for logging in using Google account
@app.route("/login/google")
def login_google():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text

    return redirect(url_for("agenda"))


# Redirected route when logging in as Google user
@app.route("/welcome/google")
@login_required
def welcome_google():

    if google.authorized:

        resp = google.get("/oauth2/v2/userinfo")
        assert resp.ok, resp.text
        email = resp.json()["email"]

    return render_template("welcome_user_google.html", email=email)


@app.route("/welcome")
@login_required # Welcome is accessible only when having logged in
def welcome_user():
    return render_template("welcome_user.html")


# Seeing how location details uses the same location as event detais, the same functionality for event details has been implemented for location details to fix missing functionality
@app.route("/events/location/detail/<id>")
def location_detail(id):
    eventsAPI = RestEvents()
    event = eventsAPI.get(id) # Getting the event based on id
    return render_template("event/event_detail.html.jinja", event=event) # Passing the event so that event data can be dynamically loaded in jinja


@app.route("/events")
def event():
    return render_template("events.html.jinja")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
