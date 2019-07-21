import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home_page():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of all precipitation values"""
    
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()

    prcp_values = []
    for date, prcp in results:
        prcp_dict = {}
        date_dict["date"] = date
        ppt_dict["prcp"] = prcp
        prcp_values.append(prcp_dict)

    return jsonify(prcp_values)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all stations"""
    
    session = Session(engine)
    results = ssession.query(Station.station).all()

    stations = []
    for station in results:
        station_dict = {}
        station_dict_name["station"] = station
        stations.append(station_dict)

    return jsonify(tobs_values)


@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of all temperature values"""
    
    session = Session(engine)
    results = ssession.query(Measurement.date, Measurement.tobs).filter(Measurement.date>'2016-08-23').all()

    tobs_values = []
    for date, tobs in results:
        tobs_dict = {}
        date_dict_tobs["date"] = date
        temp_dict["tobs"] = tobs
        tobs_values.append(tobs_dict)

    return jsonify(tobs_values)

@app.route("/api/v1.0/<start>")
def tobs_start():
    
    
    session = Session(engine)
    results = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date>='start_date').all()
    print(results)

@app.route("/api/v1.0/<start>/<end>")
def tobs_startend():
    
    
    session = Session(engine)
    results = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date>='start_date').filter(Measurement.date<='end_date').all()
    print(results)
    

if __name__ == '__main__':
    app.run(debug=True)