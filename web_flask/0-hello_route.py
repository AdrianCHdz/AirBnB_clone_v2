#!/usr/bin/python3
"""
This python script will start a flask web app
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """This function will print a line whenever it is no the root"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
