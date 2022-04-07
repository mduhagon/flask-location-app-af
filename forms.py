from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User, Pet

class RegistrationForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired(), Length(min=3, max= 20)])
   email= StringField('Email', validators=[DataRequired(), Email()])
   password= PasswordField('Password', validators=[DataRequired()])
   confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
   #about_me=TextAreaField('About Me', validators=[DataRequired()])
   #pet_lostorfound=SelectField('Lost or Found Pet?',choices=['Lost', 'Found'], validators=[DataRequired()])
   #area=StringField('Area', validators=[DataRequired()])
   #lookup_address = StringField('Search address') ##
   #coord_latitude = HiddenField('Latitude',validators=[DataRequired()])##
   #coord_longitude = HiddenField('Longitude', validators=[DataRequired()])##
   submit= SubmitField('Register')

   def validate_username(self, username):
        user= User.query.filter_by(username=username.data).first() 
        if user:
           raise ValidationError('Username already exists. Please choose another one.')

   def validate_email(self, email):
        user= User.query.filter_by(email=email.data).first() 
        if user:
           raise ValidationError('Email already exists. Please choose another one or log in.')


class LoginForm(FlaskForm):
   email= StringField('Email', validators=[DataRequired(), Email()])
   password= PasswordField('Password', validators=[DataRequired()])
   remember= BooleanField('Remember Me')
   submit= SubmitField('Log In')
     
class LostPetForm(FlaskForm):
   description = StringField('Name your location (For ex: Dog Laika last seen here.)',
                           validators=[DataRequired(), Length(min=1, max=80)])
   lookup_address = StringField('Find the address')
   coord_latitude = HiddenField('Latitude',validators=[DataRequired()])
   coord_longitude = HiddenField('Longitude', validators=[DataRequired()])                    
   submit = SubmitField('Save location on map')
    
class FoundPetForm(FlaskForm):   
   description = StringField('Name your location (For ex: Husky found here.)',
                           validators=[DataRequired(), Length(min=1, max=80)])
   lookup_address = StringField('Find the address')
   coord_latitude = HiddenField('Latitude',validators=[DataRequired()])
   coord_longitude = HiddenField('Longitude', validators=[DataRequired()])                    
   submit = SubmitField('Save location on map')

class NewLocationForm(FlaskForm):
    description = StringField('Location description',
                           validators=[DataRequired(), Length(min=1, max=80)])
    lookup_address = StringField('Search address')

    coord_latitude = HiddenField('Latitude',validators=[DataRequired()])

    coord_longitude = HiddenField('Longitude', validators=[DataRequired()])                    

    submit = SubmitField('Create Location')

