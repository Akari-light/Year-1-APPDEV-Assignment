from wtforms import StringField, PasswordField, BooleanField, SelectField, TextAreaField, RadioField, IntegerField
from wtforms.fields.html5 import IntegerField, DateField
from wtforms.validators import *
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[InputRequired(), Length(min=4, max=35)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=80)])
    remember = BooleanField('Remember Me')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=1, max=25)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=25)])
    email = StringField('Email Address', validators=[InputRequired(), email("Email is invalid or already taken")])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match'), Length(min=4, max=80)])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I agree the user agreement and Terms & Conditions', validators=[DataRequired()])

        
class PatientInformationForm(FlaskForm):
    nric = StringField('Birth Certificate:', validators=[Length(min=1, max=150), DataRequired()])
    address = StringField('Home Address:', validators=[Length(min=1, max=300), DataRequired()])
    postal_code = IntegerField('Postal Code:', validators=[Length(min=6, max=6), DataRequired()])
    date_of_birth = DateField('Date Of Birth:', validators=[DataRequired()], format='%Y-%m-%d')
    contact_no = IntegerField('Contact Number:', validators=[Length(min=8, max=8), DataRequired()])
    gender = SelectField('Account Type', validators=[DataRequired()], choices=[('M', 'Male'), ('F', 'Female')])
    race = SelectField('Account Type', validators=[DataRequired()], choices=[('C', 'Chinese'), ('M', 'Malay'), ('I', 'Indian'), ('O', 'Others')])
    nationality = SelectField('Account Type', validators=[DataRequired()], choices=[('S', 'Singaporean'), ('PR', 'Singapore PR'), ('F', 'Foreigner')])
    medication = TextAreaField('Medication:', validators=[Optional()])

class AdminAccountUpdate(FlaskForm):
    account_type = SelectField('Account Type', choices=[('A', 'Admin'), ('S', 'staff'), ('D', 'Doctor'), ('P', 'Patient')])
    email = StringField('Email Address', validators=[InputRequired(), email("Email is invalid or already taken")])

class PatientAccountUpdate(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=1, max=25)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=25)])
    email = StringField('Email Address', validators=[InputRequired(), email("Email is invalid or already taken")])
    birth_cert = StringField('Birth Certificate:', validators=[Length(min=1, max=150), DataRequired()])
    home_addr = StringField('Home Address:', validators=[Length(min=1, max=300), DataRequired()])
    telephone = StringField('Telephone Number:', validators=[Length(min=1, max=150), DataRequired()])
    medication = TextAreaField('Medication:', validators=[Optional()])

class CreateMedForm(FlaskForm):
    med_name = StringField('Medicine Name', [Length(min=1, max=150), DataRequired()])
    quantity = IntegerField('Quantity', [DataRequired()])
    med_type = RadioField('Medicine Type', [DataRequired()], choices=[('P', 'Pill'), ('L', 'Liquid (Bottles of 100ml)'), ('C', 'Cream')])