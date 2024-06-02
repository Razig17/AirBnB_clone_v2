#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(e):
    """Close the current session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """State list"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
