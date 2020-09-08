#!/usr/bin/python3
"""
This python script will start a flask web app
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def sesclose(self):
    """docs"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def ultimate():
    """This function will send all the states in the storage
    to the template"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    place = storage.all(Place).values()
    states = sorted(states, key=lambda states: states.name)
    amenities = sorted(amenities, key=lambda amenities: amenities.name)
    place = sorted(place, key=lambda place: place.name)

    return render_template('100-hbnb.html', stateobj=states,
                           amenityobj=amenities, placeobj=place)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
