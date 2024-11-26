from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_name = 'Anubhav'
    letters = list(my_name)
    pup_dict = {'pup_name':'Sammy'}
    return render_template('index.html',my_var=my_name,letters=letters,
                           pup_dict=pup_dict)

if __name__ == '__main__':
    app.run(debug=True)