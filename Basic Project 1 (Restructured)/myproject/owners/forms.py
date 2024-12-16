from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):
    
        name = StringField('Name of Puppy:')
        pup_id = IntegerField("Id of Puppy: ")
        submit = SubmitField('Add Puppy')