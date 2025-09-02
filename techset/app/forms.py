from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, BooleanField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rmr_me = BooleanField('Remember Me?')
    submit = SubmitField('Sign In')