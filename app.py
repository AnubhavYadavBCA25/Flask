from flask import Flask

## WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my Web Application! Please Visit."

@app.route('/model')
def ml_model():
    return "This is a machine learning model."

if __name__ == '__main__':
    app.run(debug=True)
