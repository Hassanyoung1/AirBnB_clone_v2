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

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Function to be called when the application context is popped.
    It ensures that the storage is properly closed.

    Parameters:
    - exception (Exception): The exception,
      if any, that triggered the teardown.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """
    Route to display a sorted list of states.

    Returns:
    - HTML: Rendered template displaying the sorted list of states.
    """
    all_state = list(storage.all(State).values())
    sorted_state = sorted(all_state, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5043, debug=True)
