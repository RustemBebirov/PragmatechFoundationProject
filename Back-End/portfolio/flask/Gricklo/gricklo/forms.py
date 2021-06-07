from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,FileField,SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(),Length(min=3, max=30)])
    username = StringField("Username", validators=[DataRequired(),Length(min=3, max=30)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6, max=20)])
    confirm = PasswordField("Password Confirm", validators=[DataRequired(),EqualTo('password')])
    phone = StringField("Phone", validators=[DataRequired(),Length(min=9,max=20)])
    image = FileField("Image")
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = username = StringField("Username", validators=[DataRequired(),Length(min=3, max=30)])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6, max=20)])
    submit = SubmitField("Login")