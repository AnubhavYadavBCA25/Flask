# Converting original name to latin name

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Welcome to the latin name conversion website!</h1>"

@app.route('/puppy/<name>')
def latin_name(name):
    if name[-1] != 'y':
        return "Hi "+name+"! Your latin name is "+name+'y.'
    elif name[-1] == 'y':
         return "Hi "+name+"! Your latin name is "+name[0:len(name)-1]+'iful.'

if __name__ == "__main__":
    app.run(debug=True)