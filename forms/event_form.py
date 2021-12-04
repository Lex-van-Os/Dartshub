# modules to create a flask form
from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, validators, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email


# form to post data
class EventsForm(FlaskForm):

    FirstName = StringField("Voornaam: ", [validators.required()])
    LastName = StringField("Achternaam: ", [validators.required()])
    Email = StringField("Email address: ",
                        validators=[DataRequired(), Email()])
    Telephone = IntegerField('Telefoonnummer: ', [validators.required()])
    Description = StringField("Opmerkingen: ", [validators.required()])
    Dates = StringField("Op welk datum zou u willen spelen?: ",
                        [validators.required()])
    Locations = SelectMultipleField("Locations: ",
                                    choices=[("Amsterdam"), ("Rotterdam"),
                                             ("Den Haag")])
    Age = BooleanField("18 jaar ? ")
    Payment = SelectMultipleField("Betaalmogelijkheden: ",
                                  choices=[("Tikkie"), ("Creditcart"),
                                           ("Cash")])
    Submit = SubmitField("Versturen")
