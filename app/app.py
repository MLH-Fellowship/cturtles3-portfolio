from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    # rid (port="5002") within run function
    app.run() 