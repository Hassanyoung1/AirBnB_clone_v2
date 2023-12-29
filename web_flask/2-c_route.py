#!/usr/bin/python3
"""Importing flash module"""
from flask import Flask

"""
a script that starts a Flask web application:
listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_root():
    """ Display hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Display hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):

    """
    Display text passed in as an argument
    Replace underscore symbols with a space
    return: The argument pased
    """

    text = text.replace('_', '')
    return f"C {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
