#!/usr/bin/python3

"""
This script defines a Flask web application that serves as a storage interface
for fetching data from a storage engine.
It includes a route '/cities_by_states'
to display a sorted list of states using a template.

Usage:
- Run the script to start the Flask application.
- Access the '/cities_by_states' route in a
web browser to view the list of states.

Dependencies:
- Flask
- models (imported from models module)
- models.state.State (imported from models.state module)

Note: Make sure to have the necessary dependencies installed before running
the script.
"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """A method to remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """A method to render an HTML page with a list of all State objects
    """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
