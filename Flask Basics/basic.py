# Import Flask Class from flask module
from flask import Flask

# Creating an app variable
app = Flask(__name__)

# Creating a route decorator and a function to return a string
@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

if __name__ == "__main__":
    app.run()