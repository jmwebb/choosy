from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import TextField


class LoginForm(FlaskForm):
	username = TextField('Username')
	password = PasswordField('Password')