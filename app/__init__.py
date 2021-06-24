from flask import Flask, render_template, url_for, request, redirect, json, Response
import os
import json
from . import db


app = Flask(__name__)
data_file = open('./app/static/data.json')
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
