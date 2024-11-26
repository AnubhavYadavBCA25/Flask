from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_lst = [1,2,3,4,5]
    puppies = ['Sammy','Frankie','Rosie']

    # Real world example
    user_logged_in = True 
    return render_template('index2.html',my_lst=my_lst,puppies=puppies,
                           user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug=True)