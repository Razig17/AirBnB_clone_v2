#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """display C followed by the value of the text variable"""
    return "C " + text.replace("_", " ")


@app.route('/python/<text>')
def python(text):
    """Display Python followed by the value of the text variable"""
    if text:
        return "Python " + text.replace("_", " ")
    return "Python is cool"


app.route('/python')
def just_python(text):
    """Display Python is cool"""
    return "Python is cool"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
