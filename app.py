from flask import Flask, redirect, url_for

## WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my Web Application! Please Visit."

@app.route('/model')
def ml_model():
    return "This is a machine learning model."

#### Building URL Dynamically ####
# Variable Rules and URL Building
@app.route('/success/<int:score>')
def success(score):
    return "The student has acheived marks "+ str(score)

@app.route('/fail/<int:score>')
def failed(score):
    return "The student has failed with marks "+ str(score)

# Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks<50:
        result = 'failed'
    else:
        result = 'success'
    
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    app.run(debug=True)
