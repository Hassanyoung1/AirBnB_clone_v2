#!/usr/bin/python3
"""Importing flask module"""

from flask import Flask, render_template

"""
a script that starts a Flask web application:
listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
/python/<text>: display “Python ” followed by the value of the text variable
(replace underscore _ symbols with a space )
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
    return: The argument passed
    """

    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is_cool'},
           strict_slashes=False)
def display_txt_default(text):
    """
    Display text passed in as an argument
    Replace underscore symbols with a space
    return: The argument passed
    """

    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Display that n is a number if n is an integer
    return: The formatted string indicating that n is a number
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders an HTML template with the provided number.

    Args:
        n (int): The number to be displayed in the template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Renders an HTML template with the provided number and its odd/even status.

    Args:
        n (int): The number to be displayed in the template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
