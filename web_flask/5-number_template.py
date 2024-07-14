#!/usr/bin/python3
'''
Creates a flask app
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Home route'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Home route'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    '''Takes a text and uses it'''
    clean_text = text.replace('_', ' ')
    return "C " + clean_text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    '''Text with a default value'''
    clean_txt = text.replace('_', ' ')
    return "Python " + clean_txt


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Only if n is a number'''

    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    '''Only if n is a number in a template'''

    return render_template("5-number.html", num=n)

if __name__ == '__main__':
    app.run()
