from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

# Using Bcrypt to hash passwords
bcrypt = Bcrypt()

password = 'SuperSecretPassword'

hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

print(hashed_password)

check = bcrypt.check_password_hash(hashed_password, 'superSecretPassword')

print(check)

# Using Werkzeug to hash passwords
hashed_password = generate_password_hash(password)

print(hashed_password)

check2 = check_password_hash(hashed_password, 'superSecretPassword')

print(check2)