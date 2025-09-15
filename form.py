from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class Form(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Enter your name"})
    email = StringField("Email: ", validators=[DataRequired(), Email(message="Please enter a correct email address")], render_kw={"placeholder": "Enter your email"})
    phone_number = StringField("Phone Number: ", validators=[DataRequired(), Length(min=10, max=15)], render_kw={"placeholder": "Enter your phone number"})
    message = TextAreaField("Message: ", validators=[DataRequired(), Length(min=10, max=500)], render_kw={"placeholder": "Enter your message"})
    submit = SubmitField("SEND")


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email"})
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Enter your password"})
    submit = SubmitField("Login")