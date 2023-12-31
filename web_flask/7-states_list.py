#!/usr/bin/python3

"""
storage for fetching data from the storage engine
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    all_state = list(storage.all(State).values())
    sorted_state = sorted(all_state, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5033, debug=True)
