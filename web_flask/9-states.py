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


@app.route('/states', defaults={"id": 1}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """

    """
    if id == 1:
        states = storage.all(State)
        return render_template('9-states.html', states=states)
    else:
        for state in storage.all(State).values():
            if state.id == id:
                return render_template('9-states.html', state=state)
        return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
