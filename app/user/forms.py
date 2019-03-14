from flask_wtf import FlaskForm
from wtforms import validators, StringField, IntegerField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField

class SignupForm(FlaskForm):
	name = StringField("Name:", [validators.DataRequired()])
	email = EmailField("Email:", [validators.DataRequired(), validators.Email()])
	password = PasswordField("Password", [validators.DataRequired()])
	password_conf = PasswordField("Confirm Password", [validators.DataRequired()])
	submit = SubmitField('Signup!')

class LoginForm(FlaskForm):
	email = EmailField("Email:", [validators.DataRequired(), validators.Email()])
	password = PasswordField("Password", [validators.DataRequired()])
	submit = SubmitField('Login!')