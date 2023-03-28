'''
Created on 

Course work: Mar 27, 2023

@author: 
    Bagiya

Source:
'''


from flask import Flask, render_template, request
import mysql.connector

import db_config as dbc

app = Flask(__name__)

# configure MySQL database connection

mydb = mysql.connector.connect(host = "localhost", user = "bagiya",passwd = "Bagiya@05", database = "mlmodel")  


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


if __name__ == '__main__':
    app.run(debug=True, 
            host='0.0.0.0', 
            port=7462)