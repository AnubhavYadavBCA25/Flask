import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Now we can create our db instance
db = SQLAlchemy(app)

# And also our Migrate instance
Migrate(app, db)

#############################################################################################

class Puppy(db.Model):
    
    # Manual table name choice
    __tablename__ = 'puppies'

    # Primary Key column, unique id for each puppy
    id = db.Column(db.Integer, primary_key=True)
    # Puppy name
    name = db.Column(db.Text)
    # Puppy age
    age = db.Column(db.Integer)
    # Puppy breed
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        # This is the string representation of a puppy in the model
        return f"Puppy {self.name} is {self.age} years old."
    
