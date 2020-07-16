#THIS IS BROKEN. WILL FIX!!!!!

from flask import Flask, jsonify
import sqlalchemy
import numpy as np
import pandas as pd
import arrow




from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///Instructions/Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
keys = Base.classes.keys()
session = Session(engine)
Measurement= Base.classes.measurement
Station = Base.classes.station
lastdate = session.query(func.max(Measurement.date)).\
            scalar()
            
a_maxdate = arrow.get(lastdate)
startdate = a_maxdate.shift(months=-12).format('YYYY-MM-DD')


dates = []
precip = []
for row in query:
    measurement = row
    dates.append(measurement.date)
    precip.append(measurement.prcp)
measurement = pd.DataFrame({"date":dates,
                             "precipitation":precip})
measurement.dropna(inplace = True)

app = Flask(__name__)


@app.route("/")
def welcome():
    return (
        f"<h1>Welcome to my climate app</h1><br/>" 
        f"<h2>This is the solution for #2 on the sqlalchemy-challenge</h2><br/>"
        f"<br/>"
        f"<h3>Available routes</h3><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    query = session.query(Measurement).\
            filter(Measurement.date.between(startdate,lastdate)).\
            all()
    return jsonify(measurement)




if __name__ == "__main__":
    app.run(debug=False)