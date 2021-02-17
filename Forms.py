from wtforms import StringField, PasswordField, BooleanField, SelectField, TextAreaField, RadioField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import *
from flask_wtf import FlaskForm

#Webpages

#Account Management
class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=80)])
    remember = BooleanField('Remember Me')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=1, max=25)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=25)])
    email = StringField('Email Address', validators=[InputRequired(), email("Email is invalid or already taken")])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match'), Length(min=4, max=80)])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I agree the user agreement and Terms & Conditions', validators=[DataRequired()])

class AdminAccountUpdate(FlaskForm):
    account_type = SelectField('Account Type', choices=[('A', 'Admin'), ('S', 'staff'), ('D', 'Doctor'), ('P', 'Patient')])
    email = StringField('Email Address', validators=[InputRequired(), email("Email is invalid or already taken")])

#Users Information
class UserInformationForm(FlaskForm):
    nric = StringField('Birth Certificate:', validators=[Length(min=1, max=150), DataRequired()])
    address = StringField('Home Address:', validators=[Length(min=1, max=300), DataRequired()])
    postal_code = StringField('Postal Code:', validators=[Length(min=6, max=6), DataRequired()])
    date_of_birth = DateField('Date Of Birth:', validators=[DataRequired()], format='%Y-%m-%d')
    contact_no = StringField('Contact Number:', validators=[Length(min=8, max=8), DataRequired()])
    gender = SelectField('Gender', validators=[DataRequired()], choices=[('', 'Gender'), ('M', 'Male'), ('F', 'Female')], default='')
    race = SelectField('Race', validators=[DataRequired()], choices=[('', 'Race'), ('C', 'Chinese'), ('M', 'Malay'), ('I', 'Indian'), ('O', 'Others')], default='')
    nationality = SelectField('Nationality', validators=[DataRequired()], choices=[('', 'Nationality'), ('S', 'Singaporean'), ('PR', 'Singapore PR'), ('F', 'Foreigner')], default='')

class UserAccountUpdate(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=1, max=25)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=25)])
    email = StringField('Email Address', validators=[InputRequired(), email("Email is invalid or already taken")])
    nric = StringField('Birth Certificate:', validators=[Length(min=1, max=150), DataRequired()])
    address = StringField('Home Address:', validators=[Length(min=1, max=300), DataRequired()])
    postal_code = StringField('Postal Code:', validators=[Length(min=6, max=6), DataRequired()])
    date_of_birth = DateField('Date Of Birth:', validators=[DataRequired()], format='%Y-%m-%d')
    contact_no = StringField('Contact Number:', validators=[Length(min=8, max=8), DataRequired()])
    gender = SelectField('Gender', validators=[DataRequired()], choices=[('', 'Gender'), ('M', 'Male'), ('F', 'Female')], default='')
    race = SelectField('Race', validators=[DataRequired()], choices=[('', 'Race'), ('C', 'Chinese'), ('M', 'Malay'), ('I', 'Indian'), ('O', 'Others')], default='')
    nationality = SelectField('Nationality', validators=[DataRequired()], choices=[('', 'Nationality'), ('S', 'Singaporean'), ('PR', 'Singapore PR'), ('F', 'Foreigner')], default='')

class CreateMedForm(FlaskForm):
    med_name = StringField('Medicine Name', [Length(min=1, max=150), DataRequired()])
    quantity = IntegerField('Quantity', [DataRequired()])
    med_type = RadioField('Medicine Type', [DataRequired()], choices=[('P', 'Pill'), ('L', 'Liquid (Bottles of 100ml)'), ('C', 'Cream')])

#Appointment name, phone, doctor, appointment_type, date, time
class CreateAppointmentForm(FlaskForm):
    doctor = SelectField('Appointment type', validators=[DataRequired()], choices=[('', 'Doctors'), ('Arvin', 'Arvin'), ('Xue Qi', 'Xue Qi'), ('Htet', 'Htet'), ('Poh Loon', 'Poh Loon')], default='')
    appointment_type = SelectField('Appointment type', validators=[DataRequired()], choices=[('', 'Appointment Type'), ('Face to face', 'Face to face'), ('Online Appointment', 'Online Appointment')], default='')
    appointment_date = DateField('Booking Date:', validators=[DataRequired()], format='%Y-%m-%d')
    appointment_time = SelectField('Time', validators=[DataRequired()], choices=[('', 'Time Slot'), ('09:00 - 10:00', '09:00 - 10:00'), ('10:00 - 11:00', '10:00 - 11:00'), ('14:00 - 15:00', '14:00 - 15:00'), ('15:00 - 16:00', '15:00 - 16:00')], default='')


