# Intergrate HTML with Flask
# HTTP verb GET and POST

from flask import Flask, redirect, url_for, render_template, request

## WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

#### Building URL Dynamically ####
# Variable Rules and URL Building
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res = 'PASS'
    else:
        res = 'FAIL'
    return render_template('result.html', result=res)

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

# Result checker HTML Page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4
    res = ""
    return redirect(url_for('success', score=total_score))

if __name__ == '__main__':
    app.run(debug=True)
