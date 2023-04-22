from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    SelectField,
    SelectMultipleField,
)
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    employee_number = StringField("Employee Number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class AssignTableForm(FlaskForm):
    tables = SelectField("Tables", coerce=int, validators=[DataRequired()])
    servers = SelectField("Servers", coerce=int, validators=[DataRequired()])
    assign = SubmitField("Assign")


class CloseTableForm(FlaskForm):
    close = SubmitField("Close Table")


class AddToOrderForm(FlaskForm):
    menu_item_ids = SelectMultipleField("Menu Items", coerce=int)
    submit = SubmitField("Add to Order")
