from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index_project():
    return render_template('index_project.html')

@app.route('/report_project')
def report_project():

    lower_case = False
    upper_case = False
    num_end = False
    username = request.args.get('username')

    lower_case = any(c.islower() for c in username)
    upper_case = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()

    report = lower_case and upper_case and num_end

    return render_template('report_project.html', report=report, lower_case=lower_case, upper_case=upper_case, num_end=num_end)


if __name__ == '__main__':
    app.run(debug=True)