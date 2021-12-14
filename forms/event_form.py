# backup voor mochten jullie de real form verneuken
# modules to create a flask form
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectMultipleField,
    SubmitField,
    validators,
    BooleanField,
    IntegerField,
)
from wtforms.validators import DataRequired, Email


# form to post data
class EventsForm(FlaskForm):

    FirstName = StringField("Voornaam: ", validators=[DataRequired()])
    LastName = StringField("Achternaam: ", validators=[DataRequired()])
    Email = StringField("Email address: ", validators=[DataRequired()])
    Telephone = IntegerField("Telefoonnummer: ", validators=[DataRequired()])
    Description = StringField("Opmerkingen: ", validators=[DataRequired()])
    Dates = StringField("Op welk datum zou u willen spelen?: ", validators=[DataRequired()])
    Locations = SelectMultipleField(
        "Locations: ", choices=[("Amsterdam"), ("Rotterdam"), ("Den Haag")]
    )
    Age = BooleanField("18 jaar ? ")
    Payment = SelectMultipleField(
        "Betaalmogelijkheden: ", choices=[("Tikkie"), ("Creditcart"), ("Cash")]
    )
    Submit = SubmitField("Versturen")
