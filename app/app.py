from flask import Flask, render_template, url_for, request, redirect
import os

app = Flask(__name__)

#Create URL routes
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/home')
def home():
    return render_template("home.html")

#Create URL for each members
@app.route('/about/<string:name>')
def about(name):
    return render_template("about.html", name=name)


if __name__ == "__main__":
    # rid (port="5002") within run function
    app.run(debug=True) 
