# Do all my imports here. 
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
import numpy as np
import pandas as pd
import datetime as dt

#################################################
# Database Setup
#################################################
# From Jupyter notebook file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
MeasurementTable = Base.classes.measurement
StationTable = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

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