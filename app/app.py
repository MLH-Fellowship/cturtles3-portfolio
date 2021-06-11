from flask import Flask, render_template, url_for, request, redirect, json
import os
import json

app = Flask(__name__)
data_file = open('./app/static/data.json')
data = json.load(data_file)
#data_file.close()

#Create URL routes
@app.route('/')
def home():
    allUsers = data
    return render_template("home.html", allUsers=allUsers)

#Create URL for each members
@app.route('/about/<string:name>')
def about(name):
    userData = data[name]
    allUsers = data
    return render_template("about.html", name=name, userData=userData, allUsers=allUsers)

