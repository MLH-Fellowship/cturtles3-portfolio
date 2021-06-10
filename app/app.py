from flask import Flask, render_template, url_for, request, redirect
import os
import json

app = Flask(__name__)
data_file = open('./static/data.json')
data = json.load(data_file)
data_file.close()

#Create URL routes
@app.route('/')
def home():
    userData = data
    return render_template("home.html", userData=userData)

#Create URL for each members
@app.route('/about/<string:name>')
def about(name):
    userData = data[name]
    return render_template("about.html", name=name, userData=userData)


if __name__ == "__main__":
    # rid (port="5002") within run function
    app.run(debug=True) 
