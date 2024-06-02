#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(e):
    """Close the current session"""
    storage.close()


@app.route("/states")
def states_list():
    """Display a HTML page with a list of all the states"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route("/hbnb_filters")
def hbnb_filters():
    """
    List a state with the list of City objects linked to the State
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
