from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo



class Character_creation(FlaskForm):
    name = StringField("Enter the name of your Champion", validators=[DataRequired()])
    