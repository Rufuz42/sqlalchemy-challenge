# Do all my imports here. 
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
import numpy as np
import datetime as dt

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Creates the server
app = Flask(__name__)

# Home route
@app.route('/')
def homepage():
    return(
        f'<center><h1>Homepage of the Hawaii Climate Analysis Local API</h1></center>'
        f'<center><h3>List of available routes:</h3></center>'
        f'<center>/api/v1.0/precipitation</center>'
        f'<center>/api/v1.0/stations</center>'
        f'<center>/api/v1.0/tobs</center>'
        f'<center>/api/v1.0/[start]</center>'
        f'<center>/api/v1.0/[start]/[end]</center>'
        )

# Precipritation route
@app.route('/api/v1.0/precipitation')
def precipritation():

# Launches it so I can see results of imported routes
if __name__ == '__main__':
    app.run(debug=True)