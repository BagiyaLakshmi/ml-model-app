'''
Created on : Mar 27, 2023

Course work : Flask & ml-model

@author: 
    Bagiya

Source:
'''
from flask import Flask, render_template, request
import pickle
import db_config as dbc

app = Flask(__name__)

# configure MySQL database connection


model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    user     = request.form['username']
    password = request.form['password']

    # check if the username and password are valid
    result = dbc.getcredentials(user, password)
    if result == True:
        # if the username and password are valid, redirect to the ml project page 
        return render_template('home.html')
    else:
        # if the username and password are not valid, redirect back to the login page
        return render_template('login.html', error='Invalid username or password')

@app.route("/predict", methods=['post'])
def pred():
    features= [float(i) 
                for i in 
                (request.form.values())]
    pred = model.predict([(features)])
    # pred = round(pred[0],2)
    pred = str(pred)
    pred=pred[1:-1]
    return render_template("success.html",
                           data=pred)


if __name__ == '__main__':
    app.run(debug=True, 
            host='0.0.0.0', 
            port=7462)