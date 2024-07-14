#!/usr/bin/python3
'''
Creates a flask app
'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Home route'''
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Home route'''
    return 'HBNB!'

if __name__ == '__main__':
    app.run()
