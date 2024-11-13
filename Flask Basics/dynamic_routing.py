# Import flask library
from flask import Flask

# Create an app instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

# Create a route decorator for /info
@app.route('/info')
def info():
    return '<h1>Puppies are cute!</h1>'

# Create a route decorator for /puppy/<name>
@app.route('/puppy/<name>')
def puppy(name):
    return '<h1>This is a page for {}<h1>'.format(name.upper())

if __name__ == "__main__":
    app.run()