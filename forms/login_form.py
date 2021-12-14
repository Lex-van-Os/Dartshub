# backup voor mochten jullie de real form verneuken
# modules to create a flask form
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField, SubmitField, PasswordField)
from wtforms.validators import DataRequired, Email


# form to login
class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Verstuur")


# form to post data
class RegisterForm(FlaskForm):

    email = StringField("Email address: ",
                        validators=[DataRequired(), Email()])
    username = StringField("Gebruikersnaam: ", validators=[DataRequired()])
    password = PasswordField("Wachtwoord: ", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Verstuur")
