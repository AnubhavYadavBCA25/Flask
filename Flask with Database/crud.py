from basic import db, Puppy

# Create #
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# Read #
all_puppies = Puppy.query.all()
print(all_puppies)

# Select by ID #
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# Filters #
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

# Update #
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# Delete #
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

# Check #
all_puppies = Puppy.query.all()
print(all_puppies)

# Note: We only run this crud.py file once, and if we run it again, it will give us an error because the data is already in the database.
# To run this file again, we have to delete the data data.sqlite file and run the setupdatabase.py file again. (For Practice)