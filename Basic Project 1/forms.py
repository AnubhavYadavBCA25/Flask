from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):
    
        name = StringField('Name of Puppy:')
        submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
        
        id = IntegerField('ID Number of Puppy to Remove:')
        submit = SubmitField('Remove Puppy')

class AddOwner(FlaskForm):
    
        name = StringField('Name of Owner:')
        pup_id = IntegerField('ID of Puppy:')
        submit = SubmitField('Add Owner')