from flask import Flask, render_template, url_for, request, redirect, json, Response
import os
import json
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db

app = Flask(__name__)
data_file = open('static/data.json')
data = json.load(data_file)
#data_file.close()

#dB
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)


#Create URL routes
@app.route('/')
def home():
    allUsers = data
    return render_template("home.html", allUsers=allUsers)

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
	        'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = "User {username} is already registered."

        if error is None:
            db.execute(
	            'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return f"User {username} created successfully\n"
        else:
            return error, 418

    ## TODO: Return a restister page
    #return "Register Page not yet implemented", 501
    return render_template("register.html")

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
                
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful\n", 200
        else:
            return error, 418
	
    ## TODO: Return a login page:
    #return "Login Page not yet implemented", 501 
    return render_template("login.html")   

@app.route('/health')
def starting_url():
    status_code = Response(status=200)
    return status_code

#app.run(host="0.0.0.0", port=5000)

#Create URL for each members
@app.route('/about/<string:name>')
def about(name):
    userData = data[name]
    allUsers = data
    return render_template("about.html", name=name, userData=userData, allUsers=allUsers)



if __name__ == "__main__":
    # rid (port="5002") within run function
    app.run(debug=True) 
