# Import Flask
from flask import Flask

# Create an app instance
app = Flask(__name__)

# Create a route decorator
@app.route('/') # 127.0.0.1:5000/
def index():
    return '<h1>Hello Puppy!</h1>'

# Create a route decorator for /info
@app.route('/info') # 127.0.0.1:5000/info
def info():
    return '<h1>Puppies are cute!</h1>'

if __name__ == "__main__":
    app.run()