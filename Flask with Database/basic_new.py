# Create entries into the tables
from models import db, Puppy, Toy, Owner

# Create the tables in the database
db.create_all()

# Create 2 puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add puppies to database
db.session.add_all([rufus, fido])
db.session.commit()

# Check
print(Puppy.query.all())

# Grab Rufus from database
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Create a Owner for Object
rohit = Owner('Rohit', rufus.id)

# Give Rufus some toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

# Commit these changes to the database
db.session.add_all([rohit, toy1, toy2])
db.session.commit()

# Grab Rufus again after these additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Show toys
rufus.report_toys()